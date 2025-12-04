# Information Retrieval System (TF-IDF → BM25)

This project implements a simple yet powerful Information Retrieval (IR) system using Python, NLTK preprocessing, and BM25 ranking.
The system loads a dataset of articles, preprocesses the text, builds a BM25 index, and allows the user to interactively search queries from the terminal.
 ## **Features**
 * Text preprocessing (tokenization, lemmatization, stopword removal)
 * BM25 indexing using rank_bm25 
 * Interactive search from console 
 * Ranked retrieval with document snippets 
 * Works with any CSV dataset 
## **Technologies Used**
* Component	Library
* Language	Python 3
* Preprocessing	NLTK
* Ranking Model	BM25 (rank_bm25)
* Data Handling	pandas
## **Project Structure**
| IR-Assignment/ |
│ -- Code.py |
│ -- Articles.csv |
│ -- README.md |
## **Installation**
## **Install required libraries**
* Run this in VS Code / Terminal:
* pip install pandas nltk rank-bm25 scikit-learn
* Usage
Run the main script:
python Code.py
You will see:
--- Information Retrieval System Initialized (BM25) ---
Enter a query to search, or type 'quit' to exit.
Enter any query:
Enter Search Query: gold price 
The system prints top matching documents with BM25 scores.
## **How It Works**
*  Preprocessing
*  Lowercasing
*  Removing punctuation
*  Stopword removal
*  Word lemmatization
*  Token generation (required for BM25)
## ** Indexing **
Documents are converted into token lists and indexed using:
bm25 = BM25Okapi(tokenized_corpus)
Querying
Queries go through the same preprocessing and are ranked using:
scores = bm25.get_scores(processed_query)
The top-N highest scoring documents are returned.
## **Output**
```
Found 10 relevant documents:
--------------------------------------------------
RANK 1 (Score: 0.3673)
Snippet: LONDON: Gold fell back towards five-year lows on Wednesday as investors continued to pull away from the precious metal, with a slide through key chart...
--------------------------------------------------
RANK 2 (Score: 0.3672)
Snippet: strong>MUMBAI: Indian gold refiners just months ago were ramping up capacity and struggling to secure enough ore from miners. Now, they are suspending...
--------------------------------------------------
RANK 3 (Score: 0.3668)
Snippet: strong>SYDNEY: India´s gold imports could hit a record high this year amid widespread smuggling to sidestep government levies on overseas shipments, A...
--------------------------------------------------
RANK 4 (Score: 0.3526)
Snippet: strong>MANILA: Gold edged up to near its highest since June on Tuesday, as uncertainty over global growth that has hammered stocks puts the precious m...
--------------------------------------------------
RANK 5 (Score: 0.3437)
Snippet: strong>BENGALURU: Gold hit a three-week low on Thursday, after falling more than 1 percent in the previous session, as investors looked to buy into ri...
--------------------------------------------------
RANK 6 (Score: 0.3298)
Snippet: strong>SINGAPORE: </strong><strong>Gold on Friday clung to sharp overnight gains that pushed the metal to a one-year high, and looked set to post its ...
--------------------------------------------------
RANK 7 (Score: 0.3264)
Snippet: strong>MANILA: Gold climbed to a 13-month high on Friday, buoyed by gains in the euro after the European Central Bank (ECB) signalled it was done cutt...
--------------------------------------------------
RANK 8 (Score: 0.3031)
Snippet: strong>BENGALURU: Gold dropped to a seven-week low on Wednesday, driven by expectations of an early interest rate hike by the U.S. Federal Reserve.</s...```

##  **Requirements (Assignment Compliance)**

This IR system meets all assignment requirements:

 * Fully local implementation
 * No cloud-hosted vector DBs
 * TF-IDF / BM25 / Boolean retrieval
 * Reproducible pipeline
 * Clear documentation + source code included

##  Author

**Amna Ghulam Nabie**
(Amna-Ghulam-Nabie) Github



