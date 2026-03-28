import joblib
from sklearn.metrics import classification_report, confusion_matrix

model = joblib.load("src/models/phishing_model.joblib")
X_test, y_test = joblib.load("data/processed/test_data.joblib")

preds = model.predict(X_test)

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))