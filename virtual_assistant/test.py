"""import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    r.adjust_for_ambient_noise(source, duration=1)  # Helps with background noise
    print("Say something (you have 5 seconds)...")
    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        print("Got audio, recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.WaitTimeoutError:
        print("⏰ Timed out waiting for your speech.")
    except sr.UnknownValueError:
        print("🤷 Could not understand what you said.")
    except sr.RequestError as e:
        print("🧠 Could not request results from Google Speech Recognition service;", e)"""


import google.generativeai as genai
print("Gemini imported successfully")

