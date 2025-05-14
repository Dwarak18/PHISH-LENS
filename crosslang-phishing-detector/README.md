# Cross-Language Phishing Detector

This project is a cross-language phishing email and link detection system that utilizes Natural Language Processing (NLP) and machine learning techniques. The system is designed to identify phishing attempts in emails and URLs, supporting multiple languages through language detection.

## Features

- **Phishing Detection**: Uses a pre-trained machine learning model to predict whether an email or URL is a phishing attempt.
- **Multi-Language Support**: Detects the language of the input text to process emails in various languages.
- **User-Friendly Web Interface**: Provides a web application for users to input email text and URLs for phishing detection.
- **Training Capability**: Allows training of the model on phishing-related datasets in CSV format.

## Project Structure

```
crosslang-phishing-detector
├── src
│   ├── app
│   │   ├── __init__.py
│   │   ├── predict.py
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   ├── language_detection.py
│   │   └── utils.py
│   ├── webapp
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── templates
│   │   │   └── index.html
│   │   └── static
│   │       └── style.css
│   └── datasets
│       └── sample_phishing_data.csv
├── model
│   └── phishing_detector.pkl
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd crosslang-phishing-detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. To train the model, run the training script:
   ```
   python src/app/train.py
   ```

2. To start the web application, run:
   ```
   python src/webapp/main.py
   ```

3. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.