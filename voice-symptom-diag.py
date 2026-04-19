import os
import speech_recognition as sr
from gtts import gTTS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Data
Symptom = {
    "fever": "flu",
    "body aches": "flu",
    "blocked nose": "cold",
    "sore throat": "cold",
    "itchy eyes": "allergy",
    "headache": "flu"
}

Advice = {
    "flu": "Please get some rest and drink plenty of water.",
    "cold": "Keep your body warm and take vitamin C.",
    "allergy": "Try to avoid dust."
}

# 모델 학습
all_questions = list(Symptom.keys())
all_answers = list(Symptom.values())

v = TfidfVectorizer(stop_words='english') 
clf = MultinomialNB(alpha=0.1)

X = v.fit_transform(all_questions)
clf.fit(X, all_answers)

# Speaking
def Comsa_speak(my_text):
    print("[Comsa] " + my_text)
    tts = gTTS(text=my_text, lang='en')
    tts.save("test.mp3")
    os.system("afplay test.mp3") 


Comsa_speak("Hello, what symptoms are you having today?")

# listening
r = sr.Recognizer()
with sr.Microphone() as source:
    print("I'm listening!")
    audio = r.listen(source)

try:
    patient_say = r.recognize_google(audio)
    print("[Patient]" + patient_say)

    # prediction
    test_vec = v.transform([patient_say])
    diagnosis = clf.predict(test_vec)[0] 
    
    # diagnosis
    Comsa_speak("Maybe you have a " + diagnosis)
    
    # advice
    if diagnosis == "flu":
        Comsa_speak(Advice["flu"])
    elif diagnosis == "cold":
        Comsa_speak(Advice["cold"])
    elif diagnosis == "allergy":
        Comsa_speak(Advice["allergy"])
    else:
        Comsa_speak("I don't know.")

except:
    print("I can't understand your saying")

Comsa_speak("Consult a doctor. Bye!")