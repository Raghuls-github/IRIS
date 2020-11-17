from tkinter import * 
from gtts import gTTS
import os

from playsound import playsound

class Flag:
    flag=0
f=Flag()
root = Tk ()
root.geometry('350x350')
root.configure (background='black')
root.title ("Iris")
Msg = StringVar


Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(root,text ="Iris", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

def Text_to_speech():
    if f.flag==1:
        playsound('Iris.mp3')
        return
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Iris.mp3')
    playsound('Iris.mp3')
    f.flag=1

def Exit():
    root.destroy()
    os.remove('Iris.mp3')

def Reset():
    f.flag=0
    entry_field.delete(0, 'end')
    os.remove('Iris.mp3')



Button(root, font = 'arial 15 bold', text = 'PLAY', width = '4', command=Text_to_speech).place(x=25,y=140)
Button(root, font = 'arial 15 bold', text = 'EXIT', width = '4', command = Exit, bg = 'Orange').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold', text = 'RESET', width = '6', command = Reset).place(x=175 , y = 140)

root.mainloop ()

