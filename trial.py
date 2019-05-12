import wx
import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr
import win32com.client as wincl
import random
from flask import Flask, render_template

speak = wincl.Dispatch("SAPI.SpVoice")
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)
engine.runAndWait()

def say(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-18)
    engine.say(text)
    engine.runAndWait()


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/voice")
def voice():
    return render_template("voice.html")

@app.route("/medi")
def medi():
    class MyFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None,pos=wx.DefaultPosition, size=wx.Size(1250, 950),style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX| wx.CLIP_CHILDREN,
                title="Python Medical Assistant")
            panel = wx.Panel(self)
            self.SetBackgroundColour('plum')


            pic = wx.Icon("download.png", wx.BITMAP_TYPE_PNG)

            self.SetIcon(pic)
            my_sizer = wx.BoxSizer(wx.VERTICAL)
            lbl = wx.StaticText(panel,
                                label="Hello I am the Python Medical Assistant. How can I help you?")
            speak.Speak("'Welcome User !! what can I help you with ?")
            speak.Speak('Tell me your symptoms and I will find out the medicine for you')
            speak.Speak('Kindly tell me your symptoms in a single word.')
            my_sizer.Add(lbl, 0, wx.ALL, 5)
            self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(1250, 950))
            self.txt.SetFocus()
            self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
            my_sizer.Add(self.txt, 0, wx.ALL, 5)
            panel.SetSizer(my_sizer)
            self.Show()

        def OnEnter(self, event):
            input = self.txt.GetValue()
            self.txt.SetValue(input)
            pair1 = ['dizzy', "nauseated","lithargic",'restless']
            a1 = ["Try taking a XYZ medicine"]
            pair2 = ["fever", "cough", "cold", "mild chills", "high temperature"]
            a2 = ["Try taking a Ibuproven","Calpol(Paracetamol)500mg","Azithromycin 250mg","Citrizine(CTZ)","Try having a Acetaminophen(Tylenol)"]
            pair3 = ["headache","bodyache","stomachache"]
            a3 = ["Try having a aspirin + acetaminophen + caffeine"]
            pair4 = ["dental pain","teeth pain","tooth pain"]
            a4 = ["You can try out a Metrogyl Gel"]
            pair5 = ['Bye','Thanks for your help','quit']
            a5 = ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
            input = input.lower()
            if input == '':
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
            else:
                if input in pair1:
                    chat = random.choice(a1)
                    print(chat)
                    say(chat)
                if input in pair2:
                    chat = random.choice(a2)
                    print(chat)
                    say(chat)
                if input in pair3:
                    chat = random.choice(a3)
                    print(chat)
                    say(chat)
                if input in pair4:
                    chat = random.choice(a4)
                    print(chat)
                    say(chat)
                if input in pair5:
                    chat = random.choice(a5)
                    print(chat)
                    say(chat)

    if __name__ == '__main__':
        app = wx.App(True)
        frame = MyFrame()
        app.MainLoop()

@app.route("/index")
def index():
    class MyFrame(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self, None,
                              pos=wx.DefaultPosition, size=wx.Size(1250, 950),
                              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                                    wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                              title="Python Virtual Assistant")
            panel = wx.Panel(self)
            self.SetBackgroundColour('plum')
            pic = wx.Icon("download.png", wx.BITMAP_TYPE_PNG)

            self.SetIcon(pic)
            my_sizer = wx.BoxSizer(wx.VERTICAL)
            lbl = wx.StaticText(panel,
                                label="Hello I am the Python Digital Assistant. How can I help you?")
            speak.Speak("'Welcome User !! what can I help you with ?")
            speak.Speak('To begin with,either type or press the enter key so that I can recognize your voice.')

            my_sizer.Add(lbl, 0, wx.ALL, 5)
            self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(1250, 950))
            self.txt.SetFocus()
            self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
            my_sizer.Add(self.txt, 0, wx.ALL, 5)
            panel.SetSizer(my_sizer)

            self.Show()

        def OnEnter(self, event):
            input = self.txt.GetValue()
            input = input.lower()
            if input == '':
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
            else:
                try:
                    app_id = "Your App ID Here"
                    client = wolframalpha.Client(app_id)
                    res = client.query(input)
                    answer = next(res.results).text
                    print(answer)
                    engine = pyttsx3.init()
                    say(("Your answer is " + answer))
                except:
                    input = input.split(' ')
                    input = " ".join(input[0:])
                    speak.Speak("I am searching for " + input)
                    print(wikipedia.summary(input, sentences=5))
                    say(wikipedia.summary(input, sentences=5))

    if __name__ == '__main__':
        app = wx.App(True)
        frame = MyFrame()
        app.MainLoop()
if __name__ == "__main__":
    app.run(debug=True)
