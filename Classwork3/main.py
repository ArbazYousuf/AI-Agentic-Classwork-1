# Week 3 Classwork - ML, NLP and LLM Foundations

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from src import text_classification, preprocessing, tokenization, embeddings, semantic_search

parts = [
    ("Part 1: Text Classification", text_classification.run),
    ("Part 2: Text Preprocessing", preprocessing.run),
    ("Part 3: Tokenization", tokenization.run),
    ("Part 4: Embeddings and Similarity", embeddings.run),
    ("Part 5: Semantic Search", semantic_search.run),
]

if __name__ == "__main__":
    for title, func in parts:
        print("\n" + "-" * 60)
        print(title)
        print("-" * 60)
        func()
