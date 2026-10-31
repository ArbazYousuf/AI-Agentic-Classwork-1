# Part 1 - Text Classification using scikit-learn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.preprocessing import clean_text

# my small dataset of customer support messages
data = [
    ("I was charged twice for my subscription this month", "billing"),
    ("Please refund the extra payment on my credit card", "billing"),
    ("My invoice shows the wrong amount", "billing"),
    ("How do I update my payment method?", "billing"),
    ("Why did my bill increase this month?", "billing"),
    ("I need a receipt for my last payment", "billing"),
    ("Cancel my plan and stop charging my card", "billing"),
    ("The discount code was not applied to my invoice", "billing"),
    ("I was billed after I cancelled my subscription", "billing"),
    ("Can I pay annually instead of monthly?", "billing"),
    ("The app crashes every time I open it", "technical"),
    ("I cannot log in, the page keeps loading", "technical"),
    ("Error 500 appears when I upload a file", "technical"),
    ("The website is very slow today", "technical"),
    ("My password reset email never arrived", "technical"),
    ("The mobile app freezes on the home screen", "technical"),
    ("Sync is not working between my devices", "technical"),
    ("I get a blank screen after the latest update", "technical"),
    ("The export button does nothing when clicked", "technical"),
    ("Notifications stopped working on my phone", "technical"),
    ("What are your business hours?", "general"),
    ("Do you have an office in Karachi?", "general"),
    ("I love your product, great job team", "general"),
    ("How can I contact the sales department?", "general"),
    ("Are you hiring software engineers?", "general"),
    ("Where can I read your privacy policy?", "general"),
    ("Do you offer training sessions for new users?", "general"),
    ("Can I suggest a new feature?", "general"),
    ("Thank you for the quick help yesterday", "general"),
    ("Which languages does your support team speak?", "general"),
]


def run():
    texts = [clean_text(t) for t, label in data]
    labels = [label for t, label in data]

    # stratify so each class is in both train and test
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.3, random_state=42, stratify=labels
    )
    print("Total:", len(texts), "Train:", len(X_train), "Test:", len(X_test))

    # convert text to numbers with TF-IDF
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)  # only transform, don't fit on test data
    print("Vocabulary size:", len(vectorizer.vocabulary_))

    # training
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # evaluation
    y_pred = model.predict(X_test_vec)
    print("\nAccuracy:", round(accuracy_score(y_test, y_pred), 2))
    print(classification_report(y_test, y_pred, zero_division=0))

    # inference on new messages
    new_texts = [
        "I was charged for a plan I never ordered",
        "The app shows an error when I try to log in",
        "What time does your office open?",
        "Please send me a receipt for my refund",
    ]
    new_vec = vectorizer.transform([clean_text(t) for t in new_texts])
    predictions = model.predict(new_vec)
    print("Predictions on new text:")
    for text, pred in zip(new_texts, predictions):
        print(f"  {pred}: {text}")

    print("\nTraining vs Inference:")
    print("Training is when the model learns from labelled data (fit). It builds the")
    print("vocabulary and learns the weights. Inference is when we use the trained model")
    print("to predict labels for new text it has never seen (predict). No learning happens there.")
