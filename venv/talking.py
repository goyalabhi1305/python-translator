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
p1name="Abhishek Hindi"
lang_p1_speak = "hi-IN"
lang_p1_lis = "hi"

p2name="Abhishek French"
lang_p2_speak = "fr-FR"
lang_p2_lis = "fr"

def PersonTalk(pname,speak_lang,lis_lang,x,p2lis):
    try:
        with mic_voice as source:
            print("Listening for ", pname,"...")
            audio = recogniser.listen(mic_voice)
        print("Recognizing...")
        text_out_of_audio = recogniser.recognize_google(audio, language=speak_lang)
        print("Processing...")
        translate_text = translator.translate(text_out_of_audio, lang_tgt=p2lis, pronounce=True)
        translated_ver_txt = translate_text[0]
        translated_aud = translate_text[2]
        print(pname, ": '",translated_ver_txt,"'")
        speak_boice = gTTS(translated_ver_txt, slow=False, lang=p2lis)
        chat_string_name = "./chats/Person_{}.mp3".format(x)
        speak_boice.save(chat_string_name)
        playsound(chat_string_name)
    except Exception as e:
        print(e)
        print("Error !!!")
        return "None"

for x in range(0,500):
    if x%2==0:
        PersonTalk(p1name,lang_p1_speak,lang_p1_lis,x,lang_p2_lis )
    else:
        PersonTalk(p2name,lang_p2_speak,lang_p2_lis,x,lang_p1_lis )