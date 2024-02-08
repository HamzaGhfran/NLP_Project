from flask import Flask, render_template, request
import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import whoosh.index as index_module

app = Flask(__name__)

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Set up NLTK components
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Function for text summarization using NLTK
def nltk_summarizer(text):
    words = word_tokenize(text)
    summary = " ".join(words[:5])  # Join the first 50 words as a summary
    return summary

# Function for text preprocessing
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization and lowercasing
    tokens = [stemmer.stem(token) for token in tokens if token.isalnum()]  # Stemming
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
    return " ".join(tokens)

# Function for search index
def search_index(query_text):
    query_text = preprocess_text(query_text)
    ix = index_module.open_dir("/home/hamza/BSCS/Semester7/NLP/Project/index_dir")  # Replace with your index directory
    with ix.searcher() as searcher:
        query_parser = QueryParser("content", ix.schema)
        query = query_parser.parse(query_text)
        results = searcher.search(query, limit=10)  # Retrieve top 10 results

        # Create a list of dictionaries for result data
        result_data = []
        for hit in results:
            result_data.append({
                'Category': hit['category'],
                'Headline': hit['content'],
                'Author': hit['author'],
                'Link': hit['link'],
                'Short Description': nltk_summarizer(hit['short_description']),
                'Date':hit['date']
            })

        return result_data

# Route for index/homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = search_index(query)
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run()