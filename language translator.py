from tkinter import *
from tkinter import ttk
import tkinter as tk
from googletrans import Translator, LANGUAGES
from tkinter import messagebox
import speech_recognition as sr
from pygame import mixer
import os
from langdetect import detect
from gtts import gTTS

root = tk.Tk()

root.title("Language Translator 2.0")
root.geometry('550x350')
root.minsize(550, 350)
root.configure(bg="black")
root.iconbitmap(r'C:\Users\hima\Downloads\mic.ico')

app_name = Label(root, text='Language Translator', font=('oswald', 26), bg='black', fg='grey', height=2)
app_name.pack(side=TOP, fill=BOTH, pady=0)
version = Label(root, text='2.O', fg='grey', bg='black').place(x=450, y=49)

photo = PhotoImage(file=r'C:\Users\hima\OneDrive\Desktop\python_project1\Microphone.png').subsample(15, 15)
photo1 = PhotoImage(file=r'C:\Users\hima\OneDrive\Desktop\python_project1\Microphone.png').subsample(15, 15)

def translate():
    language_1 = textbox1.get("1.0", "end-1c")
    
    lan1 = auto_detect.get()
     messagebox.showerror("Language Translator 2.0", "Please choose a valid language")
        
    lan2 = choose_language.get()
    if lan2 not in choose_language['values']:
        messagebox.showerror("Language Translator 2.0", "Please choose a valid language")

    if language_1 == "":
        messagebox.showerror("Language Translator 2.0", "Please fill up the box")
    else:
        translator = Translator()
        output = translator.translate(text=language_1, src=lan1, dest=lan2)
        f"{output.origin} ({output.src}) --> {output.text} ({output.dest})"
        textbox2.insert('end', output.text)


def Translate_it():
    language_1 = textbox1.get("1.0", "end-1c")
    lan1 = auto_detect.get()
    lan2 = choose_language.get()
    translator = Translator()
    output = translator.translate(text=language_1, src=lan1, dest=lan2)
    f"{output.origin} ({output.src}) --> {output.text} ({output.dest})"
    detect_it = detect(output.text)
    result = gTTS(text=output.text, lang=detect_it, slow=False)
    result.save("Welcome.mp3")
    os.system("Welcome.mp3")


def buttonclick():
    mixer.init()
    mixer.music.load(r'C:\Users\hima\Downloads\voice-input-master\voice-input-master\chime1.mp3')
    mixer.music.play()
    read = sr.Recognizer()
    read.pause_threshold = 0.7
    read.energy_threshold = 400
    with sr.Microphone() as source:
        try:
            audio = read.listen(source, timeout=5)
            message = str(read.recognize_google(audio))
            textbox1.insert('end', message)
            mixer.music.load(r'C:\Users\hima\Downloads\voice-input-master\voice-input-master\chime2.mp3')
            mixer.music.play()
            textbox1.focus()
            textbox1.delete(0, END)
            textbox1.insert(0, message)
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError:
            print('Could not request results from Google Speech Recognition Service')
            
def Exit():
    ask = messagebox.askquestion(title='Language Translator 2.0', message='Do you want to quit?')
    if ask == 'yes':
        root.destroy()
    else:
        pass
    
   
def clear():
    textbox1.delete(1.0, 'end')
    textbox2.delete(1.0, 'end')


var = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=var, state="readandwrite", font=('sans-serif', 10, 'bold'))
auto_detect['values'] = list(LANGUAGES.values())
auto_detect.place(x=30, y=70)
auto_detect.current(0)

var1 = tk.StringVar()
choose_language = ttk.Combobox(root, width=20, textvariable=var1, state='readandwrite', font=('Arial', 10, 'bold'))

choose_language['values'] = list(LANGUAGES.values())

choose_language.place(x=290, y=70)
choose_language.current(0)

textbox1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
textbox1.place(x=10, y=100)

textbox2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
textbox2.place(x=260, y=100)

button = Button(root, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2', command=translate)
button.place(x=150, y=280)

clear = Button(root, text='Clear', relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2', command=clear)
clear.place(x=300, y=280)

speak = Button(root, image=photo, relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2',command=buttonclick)
speak.place(x=190, y=70)

translate_speech = Button(root, image=photo, relief=RIDGE, font=('verdana', 10, 'bold'), cursor='hand2',command=Translate_it)
translate_speech.place(x=450, y=70)

exit_it = Button(root, text='Exit', relief=RIDGE, font=('verdana', 10, 'bold'), cursor='hand2',
                 command=Exit)
exit_it.place(x=505, y=320)

root.mainloop()
