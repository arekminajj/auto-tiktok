import textContent
import textToSpeech
import video

text = textContent.getRandomSubmission()
textToSpeech.textToSpeech(text['text'])
video.addVoiceoverAndSubtitlesToVideo()
