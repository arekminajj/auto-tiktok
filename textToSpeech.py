from gtts import gTTS

def textToSpeech(text):
    language = 'en'
    voice = gTTS(text=text, lang=language, slow=False)
  
    voice.save("./files/voice.mp3")
    