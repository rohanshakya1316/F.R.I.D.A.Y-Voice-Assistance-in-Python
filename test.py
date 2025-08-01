import pyttsx3

# engine = pyttsx3.init()
# engine.say("Yes")
# # engine.runAndWait()


# # engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # or voices[1] for female voice
# engine.say("Yes")
# engine.runAndWait()

engine = pyttsx3.init()
print("About to say Yes")
engine.say("Yes")
engine.runAndWait()
print("Finished saying Yes")
