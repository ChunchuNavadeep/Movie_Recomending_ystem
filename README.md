#IN THIS SITE THE POSTER MAY NOT BE LOADED AS ACCESS ISSUE FROM SOURCE
# 🤖 AI Voice Assistant (Python)

A feature-rich AI Voice Assistant built using Python that can perform tasks like voice recognition, text-to-speech, web browsing, Wikipedia search, translation, and more. This project demonstrates integration of multiple APIs and libraries to create a smart assistant similar to JARVIS.

---

## 🚀 Features

* 🎤 Speech Recognition (voice input)
* 🔊 Text-to-Speech output
* 🌐 Open websites (Google, YouTube, etc.)
* 📖 Wikipedia search
* 🌍 Language translation
* 📰 News fetching (via API)
* ⏰ Date & Time updates
* 🎲 Random responses / greetings
* 📧 Send Emails (SMTP)
* 🎵 Play audio responses (gTTS + pygame)
* 🧠 Multi-threading & scheduling support

---

## 🛠️ Tech Stack

* **Python 3.10+**
* Libraries:

  * `speech_recognition`
  * `pyttsx3`
  * `gtts`
  * `pygame`
  * `wikipedia`
  * `requests`
  * `smtplib`
  * `datetime`
  * `threading`
  * `schedule`
  * `googletrans`
  * `BeautifulSoup`

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-voice-assistant.git
cd ai-voice-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install speechrecognition pyttsx3 gtts pygame wikipedia requests schedule googletrans==4.0.0-rc1 beautifulsoup4
```

### 3. Install Additional Requirements

* Install **PyAudio** (for microphone input):

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 API Setup (Optional)

* Get a News API key from: https://newsapi.org/
* Replace in code:

```python
newsapi = "YOUR_API_KEY"
```

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

Then speak commands like:

* "Open Google"
* "Search Wikipedia for AI"
* "What is the time?"
* "Translate hello to Hindi"
* "Play music"

---

## 📂 Project Structure

```
ai-voice-assistant/
│── main.py
│── requirements.txt
│── README.md
│── assets/
│── modules/
```

---

## ⚠️ Notes

* Ensure your microphone is working properly.
* Internet connection is required for APIs.
* Email feature requires enabling "less secure apps" or app password.

---

## 💡 Future Improvements

* Add GUI (Tkinter / PyQt / Streamlit)
* Integrate OpenAI / LLM for smarter conversations
* Add wake word detection ("Hey Jarvis")
* Improve NLP understanding
* Connect with IoT devices

---

## 👨‍💻 Author

**Navadeep Chunchu**
B.Tech Data Science & Engineering

---

## 📜 License

This project is for educational purposes. You can modify and use it freely.

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and share it!
