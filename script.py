from ggts import ggts
import os

f = open('text.txt')

t = f.read()
language = 'en'

audio = gTTS(text = t, lang= language, slow = False)
audio.save('text_to_speech.wav')
os.system('text_to_speech.wav')