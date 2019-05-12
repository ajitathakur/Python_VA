import os
import pyttsx3
import speech_recognition as sr
import win32com.client as wincl
os.system('color 3f')
speak = wincl.Dispatch("SAPI.SpVoice")
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)
engine.say('welcome User !!')
engine.say('what can I help you with?')
engine.runAndWait()

def say(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 22)
    engine.say(text)
    engine.runAndWait()

def OnEnter(self, event):

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                speech = r.recognize_google(audio)
                self.txt.SetValue(speech)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service;{0}".format(e))