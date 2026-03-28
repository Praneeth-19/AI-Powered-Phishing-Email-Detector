import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/Enron.csv")
OUT_PATH = Path("data/processed/emails_clean.csv")

def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(RAW_PATH)
    # The columns in Enron.csv are 'subject', 'body', 'label'
    df = df.dropna(subset=["body", "label"])
    df = df.rename(columns={"body": "email_text"})
    df.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()