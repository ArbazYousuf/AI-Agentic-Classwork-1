# Part 2 - Text Preprocessing

import re
import string


def clean_text(text, lowercase=True, remove_punct=True):
    if lowercase:
        text = text.lower()
    if remove_punct:
        text = text.translate(str.maketrans("", "", string.punctuation))
    # replace multiple spaces / tabs / newlines with one space
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def run():
    sentences = [
        "   Hello,   WORLD!!  How are   you?  ",
        "Machine\tLearning\nis   AMAZING... isn't it?",
        "Email me at: Support@Example.COM, ASAP!!!",
        "Price: $49.99 (20% OFF) - limited time!",
        "Already clean text",
    ]

    print("Cleaned sentences:")
    for s in sentences:
        print(repr(s), "->", repr(clean_text(s)))

    # sometimes we want to keep case and punctuation, e.g. for names or questions
    print("\nOnly whitespace removed:")
    for s in sentences[:2]:
        print(repr(s), "->", repr(clean_text(s, lowercase=False, remove_punct=False)))

    print("\nWhy preprocessing is useful:")
    print("- 'Hello', 'hello' and 'hello!' become the same word, so the model doesn't count them separately")
    print("- vocabulary gets smaller which helps when the dataset is small")
    print("- extra spaces and symbols are mostly noise")
    print("- but don't over clean, e.g. 'US' and 'us' mean different things")
