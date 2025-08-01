import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import music_library


recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        music = c.lower().split(" ")[1]
        link = music_library.song[music]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Friday....")
    while True:
        # Listen for the wake word "FRIDAY"
        # obtain audio from the microphone 
        r = sr.Recognizer()

        print("recognizing...")

        
        # recognize speech using google
        try: 
            with sr.Microphone() as source: 
                print("Listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)
            # print(word)
            if word.lower() == "friday":
                speak("Yes")
                time.sleep(0.5)
                # Listen for the command
                with sr.Microphone() as source: 
                    print("Friday Activating....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    # Listen for the stop word "GOODBYE FRIDAY"
                    if command.lower() == 'goodbye friday':
                        print("FRIDAY STOPPED")
                        speak("Stopping now. Goodbye.")
                        break

                    processCommand(command)

        except Exception as e: 
            print("Error; {0}".format(e))   