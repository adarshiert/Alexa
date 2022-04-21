import speech_recognition as sr
import pyttsx3
import pywhatkit

def talk(command):
    file = open("command.txt", "w")
    file.write(command)
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id)
    engine.say("I love you  Adarsh I am Playing" +command)
    engine.runAndWait()


def takecommand():
    listener= sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening.......")
            voice = listener.listen(source)
            print("Recognizing")
            command = listener.recognize_google(voice)


    except:
        print("say that again please.........")
        return "None"
    return command

while True:
    query = takecommand().lower()

    if "play" in query:
        song = query.replace("play", " ")
        talk(song)
        pywhatkit.playonyt(song, True, True)
