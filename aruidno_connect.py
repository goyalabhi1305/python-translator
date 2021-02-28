# importing libraries
import pyfirmata
import time
import pyttsx3
import speech_recognition

board = pyfirmata.Arduino('COM3')
# text to speech
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Speaking capability
recogniser = speech_recognition.Recognizer()
mic_voice = speech_recognition.Microphone()


# welcome and ask for something
# speak("Welcome to Abhishek arduino project, which LED should I turn on?")
try:
    with mic_voice as source:
        print("Listening...")
        audio = recogniser.listen(mic_voice)
    print("Processing...")
    text_out_of_audio = recogniser.recognize_google(audio, language="en-IN")
    print(text_out_of_audio)
    text_out_of_audio = "turn board LED on"
    if ("green" in text_out_of_audio and "LED" in text_out_of_audio and "on" in text_out_of_audio):
        speak("Turning on green LED")
        board.digital[9].write(1)
        time.sleep(2)
    else:
        if ("board" in text_out_of_audio and "LED" in text_out_of_audio and "on" in text_out_of_audio):
            speak("Turning on board LED")
            board.digital[13].write(1)
            time.sleep(2)
        else:
            if ("green" in text_out_of_audio and "LED" in text_out_of_audio and "off" in text_out_of_audio):
                speak("Turning off green LED")
                board.digital[9].write(0)
                time.sleep(2)
            else:
                if ("board" in text_out_of_audio and "LED" in text_out_of_audio and "off" in text_out_of_audio):
                    speak("Turning off board LED")
                    board.digital[13].write(0)
                    time.sleep(2)



except Exception as e:
    print("An error occured")
    speak("An error happened")


# arduino stuff
#
# while True:
#     speak("On")
#     board.digital[13].write(1)
#     time.sleep(2)
#     speak("Off")
#     board.digital[13].write(0)
#     time.sleep(2)