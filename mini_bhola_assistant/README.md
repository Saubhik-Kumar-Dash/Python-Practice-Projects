# 🎙️ Mini Bhola Assistant — Voice + AI Virtual Assistant

Welcome to **Mini Bhola**, a beginner-friendly Python-based virtual assistant!  
This project is powered by **voice recognition**, **AI models** (ChatGPT, Gemini, OpenRouter), and **text-to-speech** features.  
It can open websites, play music, and even answer questions using an AI API.

---

## 🧠 Features

- 🗣️ Wake word activated (`hello`)
- 🔍 Opens websites: Google, YouTube, LinkedIn, etc.
- 🎵 Plays music via YouTube
- 🧠 Uses AI to answer prompts (via API)
- 🔊 Speaks responses out loud
- 📟 Displays output in the terminal

---

## 📂 File Structure

| File Name         | Description |
|------------------|-------------|
| `main.py`        | The main logic of the assistant |
| `musicLibrary.py`| Dictionary with song names and YouTube URLs |
| `README.md`      | Project documentation (this file) |

---

## ⚙️ Setup & Installation

### 1. 📥 Clone the Repository

```
git clone https://github.com/<your-username>/mini-bhola-assistant.git
cd mini-bhola-assistant bash
```

### 2. 🐍 (Optional) Create Virtual Environment

```
python -m venv .venv
.venv/Scripts/activate  # Windows
```

### 3. 📦 Install Dependencies

```
pip install -r requirements.txt
or
pip install SpeechRecognition pyttsx3 gTTS pygame requests openai google-generativeai pyaudio pocketsphinx
```

## 🔑 Setup API Keys

### ✅ Option 1: Free AI via OpenRouter

```
openai.api_key = "your-openrouter-api-key"
openai.api_base = "https://openrouter.ai/api/v1"
```

### 💬 Option 2: ChatGPT (OpenAI)

```
openai.api_key = "your-openai-api-key"
# No need to set api_base
```

## 🎵 How to Set Up musicLibrary.py

###Create a file called musicLibrary.py in the same folder as main.py.

```
music = {
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
}
```

## 💻 Example Voice Commands

```
"hello"                 → Wake word
"open google"           → Opens Google
"play believer"         → Opens YouTube with song
"who is Elon Musk"      → AI will speak and print the answer
```

## 🚀 Run the Project

```
python main.py
```

## Output

```
Listening for wake word 'hello'...
Detected: hello
Listening for your command...
Command: open youtube
```

## 📝 Notes

  .🧠 AI output is both spoken and printed in the terminal
  .🐌 Delay in voice response? → print() the response before speaking it:

  ```
  print(response)
  speak(response)
  ```
  .🎙️ Speech-to-text is handled using SpeechRecognition
  .🔈 Speech synthesis is done using gTTS and pygame
