import speech_recognition
import pyttsx3
from gtts import gTTS
from playsound import  playsound
from google_trans_new import google_translator

engine = pyttsx3.init()
recogniser = speech_recognition.Recognizer()
aud_file = speech_recognition.AudioFile("record.wav")
mic_voice = speech_recognition.Microphone()

translator = google_translator()
listening_lan = "hi-IN"
translated_lan = "en"
with mic_voice as source:
    print("Listening...")
    audio = recogniser.listen(mic_voice)
print("Recognizing...")
text_out_of_audio = recogniser.recognize_google(audio, language=listening_lan )
print("Processing...")
translate_text = translator.translate(text_out_of_audio,lang_tgt=translated_lan,pronounce=True)
translated_ver_txt = translate_text[0]
translated_aud = translate_text[2]
print("You said: `",text_out_of_audio,"`","\nTranslated Version: `",translated_ver_txt,"`")
speak_boice = gTTS("You Said: " + text_out_of_audio + "; Translated Version: " + translated_ver_txt, slow= False )
speak_boice.save('speakvoice.mp3')
playsound("speakvoice.mp3")
engine.runAndWait()






