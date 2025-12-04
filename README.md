Information Retrieval System (TF-IDF → BM25)

This project implements a simple yet powerful Information Retrieval (IR) system using Python, NLTK preprocessing, and BM25 ranking.
The system loads a dataset of articles, preprocesses the text, builds a BM25 index, and allows the user to interactively search queries from the terminal.
 Features
 Text preprocessing (tokenization, lemmatization, stopword removal)
 BM25 indexing using rank_bm25
 Interactive search from console
 Ranked retrieval with document snippets
 Works with any CSV dataset
 Technologies Used
Component	Library
Language	Python 3
Preprocessing	NLTK
Ranking Model	BM25 (rank_bm25)
Data Handling	pandas
Project Structure
IR-Assignment/
│-- Code.py
│-- Articles.csv
│-- README.md
 Installation
 Install required libraries
Run this in VS Code / Terminal:
pip install pandas nltk rank-bm25 scikit-learn
 Usage
Run the main script:
python Code.py
You will see:
--- Information Retrieval System Initialized (BM25) ---
Enter a query to search, or type 'quit' to exit.
Enter any query:
Enter Search Query: gold price 
The system prints top matching documents with BM25 scores.
 How It Works
 Preprocessing
Lowercasing
Removing punctuation
Stopword removal
Word lemmatization
Token generation (required for BM25)
 Indexing
Documents are converted into token lists and indexed using:
bm25 = BM25Okapi(tokenized_corpus)
Querying
Queries go through the same preprocessing and are ranked using:
scores = bm25.get_scores(processed_query)
The top-N highest scoring documents are returned.
Output
Found 10 relevant documents:
--------------------------------------------------
RANK 1 (Score: 7.2519)
Snippet: Gold prices dropped sharply today after...
--------------------------------------------------
RANK 2 (Score: 6.4221)
Snippet: Investors reacted to global market...
--------------------------------------------------
📁 Dataset
Your dataset must be a CSV file containing at least one text column.
Make sure to set:
TEXT_COLUMN = 'Article'
Requirements
Python 3.7+
pandas
nltk
rank_bm25
scikit-learn