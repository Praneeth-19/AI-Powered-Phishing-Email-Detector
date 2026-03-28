# AI-Powered Phishing Email Detector

## Project Overview
The AI-Powered Phishing Email Detector is a machine learning-based security tool designed to identify and flag phishing emails. By analyzing the textual content of emails, the system provides a risk score to help users distinguish between legitimate communications and potential security threats. The project follows a complete data science pipeline, from raw data processing to a real-time Streamlit-based user interface.

## Dataset Source and License
The model is trained on a combination of several publicly available email datasets to ensure broad coverage of both phishing and legitimate email patterns:
- **Enron Email Dataset**: A large collection of legitimate corporate emails.
- **Phishing Datasets**: Includes samples from Nazario, Nigerian Fraud, SpamAssassin, CEAS_08, and Ling datasets.
- **License**: Most of these datasets are public domain or provided for research purposes. Users should refer to individual dataset repositories (e.g., UCI Machine Learning Repository, Kaggle) for specific licensing terms.

## Architecture
The system follows a modular architecture:
1.  **Data Ingestion**: `src/data/make_dataset.py` cleans and prepares raw CSV files.
2.  **Feature Engineering**: `src/features/build_features.py` uses TF-IDF vectorization to convert text into numerical features.
3.  **Model Training**: `src/models/train.py` trains a Logistic Regression model (selected for its balance of performance and interpretability).
4.  **UI/Deployment**: `src/ui/app.py` provides a Streamlit interface for real-time predictions.

## How to Run Locally

### Prerequisites
- Python 3.8+
- pip

### Installation
1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd AI-Powered-Phishing-Email-Detector
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
1.  **Process Data**:
    ```bash
    python src/data/make_dataset.py
    ```
2.  **Build Features**:
    ```bash
    python src/features/build_features.py
    ```
3.  **Train Model**:
    ```bash
    python src/models/train.py
    ```
4.  **Launch the UI**:
    ```bash
    python -m streamlit run src/ui/app.py
    ```

## Model Performance Metrics
The model was evaluated on a test set (20% of the processed data).

### Classification Report
```text
              precision    recall  f1-score   support

           0       0.99      0.97      0.98      3159
           1       0.97      0.99      0.98      2795

    accuracy                           0.98      5954
   macro avg       0.98      0.98      0.98      5954
weighted avg       0.98      0.98      0.98      5954
```

### Confusion Matrix
```text
[[3075   84]
 [  29 2766]]
```
- **0**: Safe Email
- **1**: Phishing Email

## Ethical Considerations
- **Privacy**: This tool is designed to analyze email content. Users should ensure they have the right to process the data they input. The current implementation runs locally and does not upload data to external servers.
- **False Positives/Negatives**: While the model has high accuracy (98%), it is not infallible. A "Safe" result does not guarantee an email is harmless, and a "Phishing" result might occasionally flag legitimate content.
- **Bias**: The model's performance is tied to its training data. It may be less effective against highly novel or targeted (spear-phishing) attacks not represented in the datasets.
- **Intended Use**: This tool is intended for educational and auxiliary security purposes, not as a replacement for comprehensive enterprise-grade security solutions.
