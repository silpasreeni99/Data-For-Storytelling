#Import Statements

import speech_recognition as sr # importing speech recognition package from google api
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
from googletrans import Translator


#Assistant Speaks Functions
num = 1


def assistant_speaks(output):
 global num
 num +=1
 toSpeak = gTTS(text=output, lang='en-gb', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)

def assistant_speaksSp(output):
 global num
 num +=1
 translator = Translator()
 translated = translator.translate(output,dest="es")
 toSpeak = gTTS(text=translated.text, lang='es', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)


def assistant_speaksCh(output):
 global num
 num +=1
 translator = Translator()
 translated = translator.translate(output,dest="zh-cn")
 toSpeak = gTTS(text=translated.text, lang='zh', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)

def assistant_speaksFr(output):
 global num
 num +=1
 translator = Translator()
 translated = translator.translate(output,dest="fr")
 toSpeak = gTTS(text=translated.text, lang='fr', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)

def assistant_speaksVi(output):
 global num
 num +=1
 translator = Translator()
 translated = translator.translate(output,dest="vi")
 toSpeak = gTTS(text=translated.text, lang='vi', slow=False)
 file = str(num)+".mp3"
 toSpeak.save(file)
 playsound.playsound(file, True)
 os.remove(file)

#Function to be used to read out text
def read(text, language):
    if (language=="ENGLISH"):
        assistant_speaks(text)
    elif (language=="SPANISH"):
        assistant_speaksSp(text)
    elif (language=="CHINESE"):
        assistant_speaksCh(text)
    elif (language=="FRENCH"):
        assistant_speaksFr(text)
    elif (language=="VIETNAMESE"):
        assistant_speaksVi(text)
    
