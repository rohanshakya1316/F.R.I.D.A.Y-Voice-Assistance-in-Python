# FRIDAY - Voice Assistant in Python

FRIDAY is a simple voice-controlled assistant written in Python. It can recognize speech, process commands, and perform basic tasks on your computer.

---

## 📁 Project Structure

FRIDAY/
├── pycache/

├── venv/ # Virtual environment

├── main.py # Main file to start FRIDAY

├── music_library.py # Music handling module

├── test.py # Test scripts

├── requirements.txt # Project dependencies

└── README.md # Project documentation

---

## ⚙️ Features

- Speech Recognition
- Text-to-Speech output
- Audio playback capabilities
- Windows support using `pywin32`
- Extendable and modular structure

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone (this repository's link)
cd FRIDAY

### 2. Create and Activate Virtual Environment
Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

Install all required packages listed in requirements.txt:

pip install -r requirements.txt

### ▶️ Running the Project
Once dependencies are installed, you can start FRIDAY by running:

python main.py

Ensure your microphone is connected and enabled.

### 📦 Dependencies
Some of the core libraries used:

SpeechRecognition==3.14.3

PyAudio==0.2.14

pocketsphinx==5.0.4

pyttsx3==2.99

sounddevice==0.5.2

pywin32==223

All other dependencies are listed in requirements.txt.

### 🧪 Testing

Run the test suite using:

python test.py ---> Done to test the pyttsx3

Or test modules individually.

### 🧠 Notes
Works best on Windows (due to pywin32)

For Linux/macOS, you may need alternatives for Windows-only libraries.

If PyAudio fails to install, try:

pip install pipwin
pipwin install pyaudio

### 🙋‍♂️ Author
Developed by Rohan Man Shakya
