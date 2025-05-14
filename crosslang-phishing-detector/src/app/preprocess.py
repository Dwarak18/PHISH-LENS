from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import stopwordsiso as stopwordsiso

nltk.download('stopwords')
stop_words_en = set(stopwords.words('english'))

# Get stopwords for a given language code, fallback to English
def get_stopwords(language):
    try:
        if language and language in stopwordsiso.languages():
            return set(stopwordsiso.stopwords(language))
        else:
            return stop_words_en
    except Exception:
        return stop_words_en

def clean_text(text, language=None):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    stop_words = get_stopwords(language)
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

def PreProcessEmail(text, language=None):
    return clean_text(text, language)

def preprocess_data(file_path):
    data = pd.read_csv(file_path, skiprows=1)
    data['cleaned_text'] = data['body'].apply(lambda x: clean_text(x))
    return data

def extract_features(data):
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(data['cleaned_text'])
    return features, vectorizer

def encode_labels(data):
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(data['label'])
    return labels, label_encoder