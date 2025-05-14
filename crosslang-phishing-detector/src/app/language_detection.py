import fasttext
import os
from langdetect import detect as langdetect_detect

# Path to FastText language identification model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'lid.176.bin')

def download_fasttext_model():
    import urllib.request
    url = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
    print('Downloading FastText language identification model...')
    urllib.request.urlretrieve(url, MODEL_PATH)
    print('Download complete.')

if not os.path.exists(MODEL_PATH):
    download_fasttext_model()

# Load FastText model
tf_model = fasttext.load_model(MODEL_PATH)

def detect_language(text):
    """
    Detect the language of the given text using FastText.
    If FastText confidence is low, fallback to langdetect.
    Returns the ISO 639-1 language code (e.g., 'en', 'fr', 'de').
    """
    input_text = text.replace('\n', ' ')
    predictions = tf_model.predict(input_text)
    print(f"[DEBUG] FastText predictions: {predictions}")
    lang_code = predictions[0][0].replace('__label__', '')
    confidence = predictions[1][0]
    if confidence < 0.7:
        try:
            lang_code = langdetect_detect(input_text)
            print(f"[DEBUG] langdetect fallback: {lang_code}")
        except Exception as e:
            print(f"[DEBUG] langdetect error: {e}")
    return lang_code