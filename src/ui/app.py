import streamlit as st
import joblib
import re
import os

# Set page config FIRST
st.set_page_config(page_title="Phishing Detector", layout="wide")

@st.cache_resource
def load_models():
    try:
        model = joblib.load("src/models/phishing_model.joblib")
        vectorizer = joblib.load("src/models/tfidf_vectorizer.joblib")
        return model, vectorizer
    except Exception as e:
        return None, str(e)

st.title("AI-Powered Phishing Email Detector")

model, vectorizer_or_error = load_models()

if model is None:
    st.error(f"Error loading resources: {vectorizer_or_error}")
    st.stop()

vectorizer = vectorizer_or_error

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "URL", text)
    text = re.sub(r"\S+@\S+", "EMAIL", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

email = st.text_area("Paste email content", height=200)

if st.button("Analyze"):
    cleaned = clean_text(email)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]

    if prediction == 1:
        st.error(f"Phishing detected (risk score: {prob:.2f})")
    else:
        st.success(f"Legitimate email (risk score: {prob:.2f})")
