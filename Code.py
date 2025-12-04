#Phase 1: Data Loading and Preprocessing
import pandas as pd
import re
import uuid
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from rank_bm25 import BM25Okapi  # BM25 library

#  section to limit how wide the output can be:
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 100)

# --- Configuration ---
FILE_PATH  = 'C:/Users/MPC/Desktop/IR&TM-Assignment-3/Articles.csv'
TEXT_COLUMN = 'Article' 
TOP_N_RESULTS = 10
# ---

# Download NLTK data
try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("Downloading NLTK data...")
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)

# Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Cleans, tokenizes, removes stop words, and lemmatizes the text."""
    if not isinstance(text, str):
        return []
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words and len(word) > 1]
    return words  # BM25 works on tokenized list

# Load the data
try:
    df = pd.read_csv(FILE_PATH, encoding='Windows-1252')
    print(f"Loaded {len(df)} documents.")
    df['processed_text'] = df[TEXT_COLUMN].apply(preprocess_text)
except FileNotFoundError:
    print(f"Error: File not found at {FILE_PATH}. Check your file path.")
except Exception as e:
    print(f"An error occurred during loading: {e}")

#Phase 2 - BM25 Indexing
tokenized_corpus = df['processed_text'].tolist()
bm25 = BM25Okapi(tokenized_corpus)
print(f"BM25 index created. Total documents: {len(tokenized_corpus)}")

#Phase 3 - Retrieve and Rank
def retrieve_documents(query, query_id, top_n=TOP_N_RESULTS):
    processed_query = preprocess_text(query)
    if not processed_query:
        print("Query is too short or contains only stop words.")
        return []

    scores = bm25.get_scores(processed_query)
    ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_n]

    results = []
    for rank, idx in enumerate(ranked_indices):
        if scores[idx] <= 0:
            continue
        results.append({
            'Rank': rank + 1,
            'Score': scores[idx],
            'Doc_Id': df.iloc[idx][TEXT_COLUMN],
            'Query_Id': query_id,
            'Original Text Snippet': df.iloc[idx][TEXT_COLUMN][:150] + "..."
        })
    return results

# Phase 4 - User query
def main():
    print("\n--- Information Retrieval System Initialized (BM25) ---")
    print("Enter a query to search, or type 'quit' to exit.")

    while True:
        user_query = input("\nEnter Search Query: ").strip()
        qid = uuid.uuid4()  # generate unique query ID
        if user_query.lower() == 'quit':
            print("System shut down. Goodbye!")
            break

        if not user_query:
            continue

        results = retrieve_documents(user_query, qid, TOP_N_RESULTS)

        if not results:
            print(f"No relevant documents found for '{user_query}'.")
        else:
            print(f"\n Found {len(results)} relevant documents:")
            for result in results:
                print(f"--------------------------------------------------")
                print(f"RANK {result['Rank']} (Score: {result['Score']:.4f})")
                print(f"Snippet: {result['Original Text Snippet']}")
            print("--------------------------------------------------")

if __name__ == "__main__":
    main()
