# Classwork 3 - ML, NLP & LLM Foundations

Week 3 classwork covering text classification, preprocessing, tokenization, embeddings and semantic search.

## Files

- `main.py` - runs all 5 parts
- `src/text_classification.py` - TF-IDF + Logistic Regression on support messages
- `src/preprocessing.py` - text cleaning function
- `src/tokenization.py` - BERT and GPT-2 tokenizers
- `src/embeddings.py` - sentence embeddings and cosine similarity
- `src/semantic_search.py` - simple search using embeddings
- `evidence/` - output and screenshots

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

First run downloads the models from Hugging Face so internet is needed.

## Run

```
python main.py
```

To save the output:

```
python main.py | tee evidence/output.txt
```

## Notes

**Training vs inference:** training is when the model learns from labelled data, inference is using the trained model on new data.

**Preprocessing:** makes text consistent (lowercase, no punctuation, no extra spaces) so the same word isn't counted as different features.

**Special tokens / subwords:** BERT adds [CLS] and [SEP] to every input, [PAD] is for padding. Rare words get split into smaller pieces (like un ##bel ##ie ##va ##bly) so the tokenizer can handle any word.

**Word counts vs embeddings:** word counts only match exact words, embeddings capture meaning so "cat on sofa" and "kitten on couch" are still similar.
