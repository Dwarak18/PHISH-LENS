# This file is deprecated. Please use the CLI or Flask web interface instead.
print("[DEPRECATED] The Streamlit interface is no longer supported. Please use the CLI or Flask web interface.")

import streamlit as st
from app.predict import predict_phishing, predict_phishing_proba
from app.language_detection import detect_language

st.set_page_config(page_title="Phishing & Language Detection", layout="centered")
st.title("Phishing & Language Detection")
st.write("""
Enter a suspicious message and (optionally) a URL to check if it is phishing. The app will also detect the language and show the probability of phishing.
""")

with st.form("phishing_form"):
    email_text = st.text_area("Message *", height=150, key="email_text")
    url = st.text_input("URL (optional)", key="url")
    submitted = st.form_submit_button("Check")

if submitted:
    if not email_text.strip():
        st.warning("Please enter a message to check.")
    else:
        language = detect_language(email_text)
        result = predict_phishing(email_text, url)
        proba = predict_phishing_proba(email_text, url)
        if result == 1:
            st.error(f"Result: Phishing\nProbability: {proba:.2%}")
            st.markdown(f"**This message is likely a phishing attempt.**")
        elif result == 0:
            st.success(f"Result: Legitimate\nProbability: {proba:.2%}")
            st.markdown(f"**This message is likely NOT phishing.**")
        else:
            st.info(f"Result: Unknown\nProbability: {proba:.2%}")
            st.markdown(f"**Unable to determine if this message is phishing.**")
        st.markdown(f"**Detected Language:** `{language}`")
