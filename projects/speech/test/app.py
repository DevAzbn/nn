import speech_recognition as sr
import os
import sys
import pyttsx3

rec = sr.Recognizer()

def talk(words):
	#os.system("say " + words)
	eng = pyttsx3.init(debug = True)
	voices = eng.getProperty('voices')
	for voice in voices:
		
		print(voice.id)

		eng.setProperty('voice', voice.id)

		rate = eng.getProperty('rate')
		eng.setProperty('rate', rate+50)

		volume = eng.getProperty('volume')
		eng.setProperty('volume', 1.0)

		eng.say(words)

		eng.runAndWait()

#talk('Настя, хватит кушать!')
def get_text():
	with sr.Microphone() as source:
		print('Wait command')
		rec.pause_threshold = 1
		rec.adjust_for_ambient_noise(source, duration=1)
		audio = rec.listen(source)
	try:
		text = rec.recognize_google(audio).lower()
	except sr.UnknownValueError:
		text = 'Я не поняла'
	return text

talk(get_text())
#talk('hello, world!')