# Part 3 - Tokenization

from transformers import AutoTokenizer


def run():
    bert = AutoTokenizer.from_pretrained("bert-base-uncased")
    sentence = "Tokenization helps transformers understand unbelievably long words."

    tokens = bert.tokenize(sentence)
    ids = bert.convert_tokens_to_ids(tokens)
    print("Sentence:", sentence)
    print("Tokens:", tokens)
    print("Token IDs:", ids)

    # encode() adds [CLS] and [SEP]
    encoded = bert.encode(sentence)
    print("\nWith special tokens:", bert.convert_ids_to_tokens(encoded))
    print("IDs:", encoded)

    print("\nDecoded:", bert.decode(encoded))
    print("Decoded without special tokens:", bert.decode(encoded, skip_special_tokens=True))

    print("\nBERT special tokens:")
    for name, tok in bert.special_tokens_map.items():
        print(" ", name, tok, bert.convert_tokens_to_ids(tok))

    # compare with gpt2 tokenizer
    gpt2 = AutoTokenizer.from_pretrained("gpt2")
    test_sentences = [
        sentence,
        "I love NLP!",
        "Pneumonoultramicroscopicsilicovolcanoconiosis is a lung disease.",
        "Karachi's weather is hot and humid in summer.",
    ]
    print("\nToken counts (BERT / GPT-2):")
    for s in test_sentences:
        print(f"  {len(bert.tokenize(s))} / {len(gpt2.tokenize(s))}  {s}")

    word = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    print("\nBERT splits it into:", bert.tokenize(word))
    print("GPT-2 splits it into:", gpt2.tokenize(word))

    print("\nSpecial tokens: [CLS] is added at the start (used for classification), [SEP] at the end")
    print("or between two sentences, [PAD] for padding, [UNK] for unknown and [MASK] for masked words.")
    print("Subword tokenization breaks rare words into smaller known pieces so the vocab stays")
    print("small but can still handle any word. BERT uses ## for continuation pieces, GPT-2 uses")
    print("BPE and marks spaces with G, so both give different counts.")
