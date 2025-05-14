# Cross-Language Phishing Detector

## Overview
The Cross-Language Phishing Detector is a web application that analyzes text and URLs in multiple languages to detect phishing attempts. It uses advanced NLP and machine learning models to identify phishing indicators and provides real-time alerts to users through a modern web interface.

## Features
- Multi-language support for text and URL analysis
- Detection of phishing indicators using NLP and ML models
- Real-time alerts and clear threat notifications
- User-friendly Streamlit web interface
- Model and vectorizer files managed with Git LFS

## Project Structure
```
crosslang-phishing-detector/
├── phishing_sample_text.txt
├── README.md
├── requirements.txt
├── model/
│   ├── phishing_detector.pkl
│   └── vectorizer.pkl
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── language_detection.py
│   │   ├── lid.176.bin
│   │   ├── predict.py
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   └── utils.py
│   ├── datasets/
│   │   ├── phishing_dataset.csv
│   │   ├── phishing_emails_dataset.csv
│   │   └── sample_phishing_data.csv
│   └── webapp/
│       ├── __init__.py
│       ├── main.py
│       ├── streamlit_app.py
│       ├── static/
│       │   └── style.css
│       └── templates/
│           └── index.html
└── rangen.py
```

## Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/yourusername/Phisheye.git
   ```
2. Navigate to the project directory:
   ```powershell
   cd Phisheye
   ```
3. Install the required dependencies:
   ```powershell
   pip install -r crosslang-phishing-detector/requirements.txt
   ```
4. (Optional) If you have large model or dataset files, ensure you have [Git LFS](https://git-lfs.github.com/) installed:
   ```powershell
   git lfs install
   git lfs pull
   ```

## Usage
1. Run the Streamlit web application:
   ```powershell
   streamlit run crosslang-phishing-detector/src/webapp/streamlit_app.py
   ```
2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).
3. Input the text or URL you want to analyze and click the submit button to receive feedback on potential phishing threats.

## Notes
- Large files (such as `.pkl`, `.bin`, `.csv`) are managed with Git LFS. If you clone the repository, run `git lfs pull` to download these files.
- Files over 100MB cannot be pushed to GitHub without LFS. If you encounter errors, remove large files from git history and track them with LFS.
- The `.gitignore` is set up to exclude unnecessary files and folders.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.