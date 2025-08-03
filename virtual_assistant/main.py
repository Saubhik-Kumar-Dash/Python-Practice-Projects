import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
import google.generativeai as genai

from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
# engine = pyttsx3.init() #since i'm using gTTS no need for this and speak_old()

# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

#gemini caused lot of error even after using correct API key
#import google.generativeai as genai

# genai.configure(api_key="AIzaSyCuCDbiaVbSgIOYs0KZNCwJ8BcGg-0S_Sg", transport="rest")

# free working alternate to gemini and openAI APIs
openai.api_key = "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"  # Replace with your actual key
openai.api_base = "https://openrouter.ai/api/v1"

def aiProcess(command):
    
    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # You can change this to another free model
            messages=[
                {"role": "user", "content": command}
            ]
        )
        return response['choices'][0]['message']['content']
    
#     try:
#         openai.api_key = "sk-..."  # your key here

#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are Bhola, a virtual assistant..."},
#                 {"role": "user", "content": command}
#             ]
#         )

#         return response['choices'][0]['message']['content']


    except Exception as e:      # specifically for API limit reached Errors
        print("❌ Error:", e)
        return "Sorry, I have reached my limit or encountered an error."


import speech_recognition as sr

def live_transcription():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Start speaking... (Ctrl+C to stop)")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)       # listen for 5sec
                text = recognizer.recognize_google(audio)
                print("📝 You said:", text)
            except sr.WaitTimeoutError:
                print("⏳ Timeout: No speech detected.")
            except sr.UnknownValueError:
                print("❌ Couldn't understand audio.")
            except sr.RequestError as e:
                print("🔌 API error:", e)
            except KeyboardInterrupt:
                #engine.stop()  # Gracefully stop pyttsx3 engine
                print("\n👋 Exiting live transcription.")
                break

 
def processCommand(c):
    if c.lower() in ["exit", "bye", "tata", "close"]:       # check if command has these words or not
        speak(" Goodbye! Have a great day!")
        speak(" Don't hesitate to reach out if you need anything else. Take care!")
        speak(" My Master!")
        exit()
    
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        os.system("start spotify")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in your music library.")
    else:
        # Everything else goes to OpenAI
        output = aiProcess(c)
        print("Bhola says:", output)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Bhola....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'hello'...")
                r.adjust_for_ambient_noise(source, duration=1)  # 🌟 Important!
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio)
                print("Detected:", word)

                if word.lower() == "hello":
                    speak("Ji Maalik")
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio)
                        print("Command:", command)

                        if "transcribe" in command.lower():
                            speak("Live transcription started. Press Control C to stop.")
                            live_transcription()
                        else:
                            processCommand(command)
                    

        except sr.WaitTimeoutError:
            print("⏰ Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("🤷 Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print("🔌 API error:", e)
        except KeyboardInterrupt:
            #engine.stop()  # Gracefully stop pyttsx3 engine
            print("\n👋 Exiting Bhola. Goodbye!")
            break
        except Exception as e:
            print("❌ Error:", e)

# flow summary