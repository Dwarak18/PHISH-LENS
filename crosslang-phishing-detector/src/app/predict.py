import os
from app.preprocess import PreProcessEmail
from app.language_detection import detect_language
import joblib

MODEL_PATH = os.path.join(
    "C:", os.sep, "Users", "Bixbie", "Downloads", "Phisheye",
    "crosslang-phishing-detector", "model", "phishing_detector.pkl"
)

VECTORIZER_PATH = os.path.join(
    "C:", os.sep, "Users", "Bixbie", "Downloads", "Phisheye",
    "crosslang-phishing-detector", "model", "vectorizer.pkl"
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

try:
    vectorizer = joblib.load(VECTORIZER_PATH)
except Exception as e:
    vectorizer = None
    print(f"Error loading vectorizer: {e}")

def predict_phishing(text, url):
    """
    Predict if the given email text and URL is phishing or not.
    Returns the prediction label or None if model is not loaded.
    """
    if model is None or vectorizer is None:
        print("Model or vectorizer not loaded.")
        return None
    language = detect_language(text)
    preprocessed_text = PreProcessEmail(text, language)
    input_data = preprocessed_text + " " + url
    try:
        input_vector = vectorizer.transform([input_data])
        return model.predict(input_vector)[0]
    except Exception as e:
        print(f"Prediction error: {e}")
        return None

def predict_phishing_proba(text, url):
    """
    Return the probability that the input is phishing (class 1).
    """
    if model is None or vectorizer is None:
        return 0.0
    language = detect_language(text)
    preprocessed_text = PreProcessEmail(text, language)
    input_data = preprocessed_text + " " + url
    try:
        input_vector = vectorizer.transform([input_data])
        proba = model.predict_proba(input_vector)[0][1]  # Probability of class 1
        return proba
    except Exception as e:
        print(f"Probability prediction error: {e}")
        return 0.0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Phishing Email/URL Predictor")
    parser.add_argument('--text', type=str, required=True, help='Email text to analyze')
    parser.add_argument('--url', type=str, default='', help='URL to analyze (optional)')
    args = parser.parse_args()

    language = detect_language(args.text)
    result = predict_phishing(args.text, args.url)
    proba = predict_phishing_proba(args.text, args.url)
    label = 'Phishing' if result == 1 else ('Legitimate' if result == 0 else 'Unknown')
    print(f"Detected Language: {language}")
    print(f"Phishing Prediction: {label}")
    print(f"Phishing Probability: {proba:.2%}")