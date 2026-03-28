import pandas as pd
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "URL", text)
    text = re.sub(r"\S+@\S+", "EMAIL", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

df = pd.read_csv("data/processed/emails_clean.csv")
df["clean_text"] = df["email_text"].apply(clean_text)

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Create directories if missing
Path("src/models").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

joblib.dump(vectorizer, "src/models/tfidf_vectorizer.joblib")
joblib.dump((X, y), "data/processed/features.joblib")
