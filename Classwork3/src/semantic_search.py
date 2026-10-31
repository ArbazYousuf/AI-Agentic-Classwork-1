# Part 5 - Semantic Search

from sentence_transformers import util

from src.embeddings import get_model

documents = [
    "To reset your password, click 'Forgot password' on the login page and follow the email link.",
    "Refunds are processed within 5-7 business days to the original payment method.",
    "Our support team is available Monday to Friday, 9 AM to 6 PM.",
    "You can upgrade or downgrade your subscription plan from the billing settings page.",
    "Two-factor authentication adds an extra layer of security to your account.",
    "The mobile app is available for both Android and iOS devices.",
    "Export your data as CSV or PDF from the reports section of the dashboard.",
    "We ship internationally, delivery usually takes 7-14 days depending on the country.",
    "Python is a popular programming language for machine learning and data science.",
    "Healthy eating and regular exercise improve both physical and mental well-being.",
]


def search(query, doc_embeddings, top_k=3):
    m = get_model()
    query_emb = m.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_emb, doc_embeddings)[0]
    best = scores.argsort(descending=True)[:top_k]
    return [(scores[i].item(), documents[i]) for i in best]


def run():
    # embed all documents once and keep them
    doc_embeddings = get_model().encode(documents, convert_to_tensor=True)
    print("Stored embeddings for", len(documents), "documents")

    queries = [
        "I forgot my login credentials",
        "When will I get my money back?",
        "what time can I talk to customer service",
        "Is there an app for my iPhone?",
        "tips for staying fit",
    ]
    for q in queries:
        print("\nQuery:", q)
        for rank, (score, doc) in enumerate(search(q, doc_embeddings), 1):
            print(f"  {rank}. {score:.3f}  {doc}")
