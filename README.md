# 🩺 Comsa - Voice-Based Symptom Checker

Comsa is a simple voice-interaction health assistant that classifies user symptoms using **TF-IDF + Naive Bayes** and responds with basic medical advice using text-to-speech (TTS).

---

## 🚀 Features

- 🎤 Speech-to-text symptom input (SpeechRecognition)
- 🧠 Machine learning-based symptom classification
- 📊 TF-IDF + Naive Bayes model
- 🔊 Text-to-speech response (gTTS)
- 💬 Simple conversational medical assistant

---

## 🧠 How It Works

1. User describes symptoms via voice input
2. System converts speech → text
3. TF-IDF vectorizer converts text into numerical features
4. Naive Bayes model predicts condition:
   - flu
   - cold
   - allergy
5. Predefined advice is returned via voice output

---

## 🛠 Tech Stack

- Python
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- scikit-learn (TF-IDF, Naive Bayes)

---

## 📦 Installation

```bash
pip install speechrecognition gtts scikit-learn
