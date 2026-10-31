# Part 4 - Embeddings and Semantic Similarity

from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

model = None


def get_model():
    # load only once, semantic search also uses it
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def run():
    m = get_model()
    sentences = [
        "The cat is sleeping on the sofa.",
        "A kitten is napping on the couch.",
        "I need to reset my account password.",
        "How do I change my login credentials?",
        "The stock market fell sharply today.",
    ]
    emb = m.encode(sentences, convert_to_tensor=True)
    print("Embeddings shape:", emb.shape)
    print("First 5 numbers of sentence 1:", emb[0][:5].tolist())

    pairs = [(0, 1), (2, 3), (0, 4), (2, 4), (0, 2)]
    print("\nCosine similarity:")
    for a, b in pairs:
        score = util.cos_sim(emb[a], emb[b]).item()
        print(f"  {score:.3f}  {sentences[a]} | {sentences[b]}")

    # compare with simple word counts (stop words removed)
    cv = CountVectorizer(stop_words="english")
    counts = cv.fit_transform(sentences)
    print("\nCat vs kitten sentence:")
    print("  word count similarity:", round(cosine_similarity(counts[0], counts[1])[0][0], 3))
    print("  embedding similarity:", round(util.cos_sim(emb[0], emb[1]).item(), 3))

    print("\nThe similar pairs (cat/kitten, password/login) got high scores and the unrelated")
    print("ones are close to 0. Word counts only match exact words so cat and kitten get 0,")
    print("but embeddings capture the meaning so they still score high.")
