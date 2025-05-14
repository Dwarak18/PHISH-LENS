import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from app.preprocess import PreProcessEmail

def load_and_unify_datasets():
    # Load phishing_emails_dataset.csv
    email_path = os.path.join(os.path.dirname(__file__), '../datasets/phishing_emails_dataset.csv')
    url_path = os.path.join(os.path.dirname(__file__), '../datasets/phishing_dataset.csv')
    data = []
    # Emails: treat all as phishing (label=1)
    if os.path.exists(email_path):
        df_email = pd.read_csv(email_path)
        for _, row in df_email.iterrows():
            text = str(row.get('Subject', '')) + ' ' + str(row.get('Body', ''))
            data.append({'text': text, 'url': '', 'label': 1})
    # URLs: use label from file
    if os.path.exists(url_path):
        df_url = pd.read_csv(url_path)
        for _, row in df_url.iterrows():
            data.append({'text': '', 'url': str(row['URL']), 'label': int(row['Label'])})
    df = pd.DataFrame(data)
    # Combine text and url for feature
    df['input'] = df['text'].fillna('') + ' ' + df['url'].fillna('')
    return df

def preprocess_inputs(df):
    df['input_clean'] = df['input'].apply(lambda x: PreProcessEmail(x))
    return df

def train_model(X, y):
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    model = RandomForestClassifier()
    model.fit(X_vectorized, y)
    return model, vectorizer

def save_model(model, vectorizer, model_filepath, vectorizer_filepath):
    joblib.dump(model, model_filepath)
    joblib.dump(vectorizer, vectorizer_filepath)

def main():
    df = load_and_unify_datasets()
    df = preprocess_inputs(df)
    X_train, X_test, y_train, y_test = train_test_split(df['input_clean'], df['label'], test_size=0.2, random_state=42)
    model, vectorizer = train_model(X_train, y_train)
    save_model(model, vectorizer, os.path.join(os.path.dirname(__file__), '../../model/phishing_detector.pkl'), os.path.join(os.path.dirname(__file__), '../../model/vectorizer.pkl'))
    # Evaluate
    acc = model.score(vectorizer.transform(X_test), y_test)
    print(f"Test accuracy: {acc:.3f}")
    # Show a sample prediction with probability
    from app.predict import predict_phishing, predict_phishing_proba
    sample = X_test.iloc[0]
    print(f"Sample: {sample}")
    pred = predict_phishing(sample, '')
    proba = predict_phishing_proba(sample, '')
    print(f"Predicted: {pred}, Probability of phishing: {proba:.2%}")

if __name__ == "__main__":
    main()