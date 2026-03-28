import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = joblib.load("data/processed/features.joblib")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

joblib.dump(model, "src/models/phishing_model.joblib")
joblib.dump((X_test, y_test), "data/processed/test_data.joblib")