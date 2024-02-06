import os
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from whoosh import index
from whoosh.fields import Schema, TEXT
import concurrent.futures
import time
import threading

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Define the function for text preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [stemmer.stem(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return " ".join(tokens)

# List of CSV file paths
csv_files = [
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2010.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2011.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2012.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2013.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2014.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2015.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2016.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2017.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2018.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2019.csv",
    "/home/hamza/BSCS/Semester7/NLP/Project/Dawn 2010-2021/2020.csv",
]

# Path to directory where the single index will be stored
index_directory = "/home/hamza/BSCS/Semester7/NLP/Project/index_dir"

# Define the schema for indexing
schema = Schema(
    category=TEXT(stored=True),
    content=TEXT(stored=True),
    author=TEXT(stored=True),
    link=TEXT(stored=True),
    short_description=TEXT(stored=True),
    date=TEXT(stored=True)
)

# Create or open the index
start_time = time.time()
ix = index.create_in(index_directory, schema)
writer = ix.writer()

# Lock for synchronization
lock = threading.Lock()

# Function to perform indexing for a single CSV file
def index_csv(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
        print(df['short_description'].isnull().sum())

        # Drop rows with NaN values in 'short_description'
        df.dropna(subset=['short_description'], inplace=True)

        # Check data types in 'short_description' column
        print(df['short_description'].apply(type).value_counts())

        # Convert non-string types to string in 'short_description' column
        df['short_description'] = df['short_description'].astype(str)

        def index_document(row):
            category = row['category/tags']
            content = row['headline']
            processed_content = preprocess_text(content)
            author = row['author']
            link = row['link']
            short_description = row['short_description']
            date = row['date']

            # Acquire the lock before writing to index
            with lock:
                writer.add_document(category=category, content=processed_content,
                                    author=author, link=link, short_description=short_description,date=date)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(index_document, df.to_dict('records'))

    except pd.errors.ParserError as e:
        print(f"Error parsing file {csv_file_path}: {e}")

# Use ThreadPoolExecutor for concurrent indexing of multiple CSV files
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(index_csv, csv_files)

# Commit changes and close the writer
writer.commit()

end_time = time.time()
print("Total Time: ", end_time - start_time)
