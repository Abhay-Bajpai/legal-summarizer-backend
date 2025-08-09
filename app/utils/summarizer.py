import re
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

nltk.download('punkt', quiet=True)

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def extractive_summary(text, num_sentences=3):
    text = clean_text(text)
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return '\n'.join(sentences)

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)
    scores = np.asarray(X.sum(axis=1)).ravel()
    ranked = np.argsort(scores)[::-1]
    selected = sorted(ranked[:num_sentences])
    return '\n'.join([sentences[i] for i in selected])

def summarize_text(text, length='short'):
    if length == 'short':
        k = 2
    elif length == 'medium':
        k = 4
    else:
        k = 8
    return extractive_summary(text, num_sentences=k)
