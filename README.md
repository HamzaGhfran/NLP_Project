# NLP_Project

# Title
Information retrieval system of
Dawn Newspaper
# Content
Contents
Abstract
Problem Statement
Introduction
Tools and Technologies
Architecture 
Evaluation
User Interface 
code snippet
Conclusion

# Abstract
This abstract encapsulates the creation of an information retrieval system merging Flask,
NLTK, and Whoosh. It combines Flask's web interface with NLTK's text preprocessing and
summarization, utilizing Whoosh's indexing for efficient search functionality. This system aims
to alleviate information overload by enabling streamlined access to pertinent content. Through
concurrent processing and optimized indexing, it ensures precise and rapid retrieval of data
from multiple CSV files. Ultimately, this integration of technologies forms a versatile solution,
offering a user-friendly interface for effective and tailored information retrieval across diverse
domains

# Problem Statement

Dawn News is grappling with the challenge of enhancing user experience and engagement by streamlining access to the latest news and popular articles. Their current system lacks an efficient search mechanism and struggles to highlight engaging content, leading to reader dissatisfaction and potentially missed news. To address this, Dawn News seeks a solution that swiftly connects readers with relevant articles while ensuring continuous engagement and satisfaction. By implementing an improved system with better article showcasing and a refined search function, the aim is to promptly inform readers about the latest news and offer a seamless browsing experience tailored to their interests, ultimately fostering stronger reader loyalty and increasing readership.

# Introduction

This report introduces a system developed for Dawn News, simplifying article discovery in today's information overload. Using Flask, NLTK, and Whoosh, it offers an intuitive platform for effortless news search and filtering. While not officially affiliated, it mirrors real-world scenarios, showcasing tech's role in user engagement. Exploring its architecture, text processing, search capabilities, and performance, the report demonstrates how this system redefines Dawn News interaction, revolutionizing the article discovery experience.

# Tool & Technologies
• Flask <br>
• NLTK  <br>
• Whoosh  <br>
• HTML & CSS  <br>
• Parallelism  <br>
• Synchronization  <br>
• Visual Studio Code (VS Code)  <br>
• GitHub:

# DataSet
link:

# Architecture 

With the help of the architecture of the following diagram, we can understand the process of
information retrieval (IR) −

![image](https://github.com/HamzaGhfran/NLP_Project/assets/114594956/b47eda74-cb18-4f55-a9d1-af69e023b010)
In information retrieval (IR) systems, the process of retrieving relevant information based on user queries involves several steps. Let's delve deeper into the process show in the Diagram.

Query Analysis: Understanding user intent through tokenization, stemming, and stop word removal to normalize and process queries effectively. <br>
Indexing: Document analysis for important terms and building an index structure to map terms to respective documents for efficient retrieval. <br>
Document Retrieval: Using processed queries and the index to retrieve potentially relevant documents based on keyword matching and employing algorithms for relevance determination. <br>
Result Presentation: Displaying retrieved documents in varied formats like ranked lists, query term snippets, or document summaries to aid swift information access and identification for users.

# User Interface

![image](https://github.com/HamzaGhfran/NLP_Project/assets/114594956/7cb92266-a0ef-4b94-83e6-e2726399a02f)

![image](https://github.com/HamzaGhfran/NLP_Project/assets/114594956/3a566562-a929-4485-89b6-06d66463d469)
# Conclusions

The fusion of Flask, NLTK, Whoosh, HTML, CSS, and Python's parallelism and
synchronization techniques has crafted an effective and user-centric information retrieval
system. This collaborative integration of diverse technologies has facilitated seamless access to
a plethora of articles and top stories through an intuitive user interface. Leveraging natural
language processing and full-text indexing capabilities, alongside a well-crafted interface, the
system adeptly navigates extensive content repositories. Future iterations and enhancements to
this system promise continued advancements in delivering a tailored and engaging browsing
experience, further solidifying its role in streamlining information retrieval across diverse
domains.

# Command
Create a conda env through <br>
...<br>
$ conda env create -f environment.yml<br>
...<br>
<br>
for activation env<br>
...<br>
$ conda activate Nlp<br>
...<br>

for deactivate<br>

... <br>
$ conda deactivate Nlp<br>
...<br>

for indexing you can get dataset above link<br>
for indexing enter code folder and give path where you want to create index_dir<br>
...<br>
index_directory = "local_path"<br>
... <br>
run<br>
...<br>
python indexing.py<br>
...<br>
for searching go to /Nlp_project/app<br>
...<br>
python app.py<br>
...<br>
make sure change your local path in index_dir









