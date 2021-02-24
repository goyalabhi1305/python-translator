import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takCommand():

    r = sr.Recognizer()


    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.phrase_threshold = 1
            audio = r.listen(source)
        print("Recog...")
        query= r.recognize_google(audio, language="en-in")
        print("you said:", query)

    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hello Mr. DJ")
    takCommand()
