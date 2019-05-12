import wx
import wolframalpha
import wikipedia
import os
import pyttsx3
import speech_recognition as sr
import win32com.client as wincl

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

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(550, 550),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                                wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Python Virtual Assistant")
        panel = wx.Panel(self)
        self.SetBackgroundColour('blue')

        pic = wx.Icon("download.png",wx.BITMAP_TYPE_PNG)
        self.SetIcon(pic)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Hello I am the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(500, 500))

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
                app_id = "Your Wolframalpha API Id."
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print(answer)
                engine = pyttsx3.init()
                say((answer))
            except:
                input = input.split(' ')
                input=" ".join(input[0:])
                speak.Speak("I am searching for "+input)
                print(wikipedia.summary(input,sentences=2))
                say(wikipedia.summary(input,sentences=2))


if __name__ == '__main__':
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
