from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3
import speech_recognition as s
import threading

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

# pyttsx3 for audio
bot = ChatBot("My Bot")

conversation = [
    'hello',
    'hey',
    'hola',
    'Hi',
    'hi',
    'Hey'
    'What is your name?',
    'My name is Bot , I am created by Atul',
    'How are you?',
    'I am doing great these days',
    'Thanks',
    'Where are you from?',
    'I am from Patna',
    'In which language do you talk?',
    'I talk mostly in English'
    'Bye'
    'Goodbye'
    ]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(conversation)

# code without GUI

#print("Talk to My Bot")
#while True:
#    print("you : ", end='')
#    query = input()
#    if query == 'exit':
#        break
#    answer = bot.get_response(query)
#    print("bot :",answer)

main = Tk()

main.geometry("400x570")
main.title("Chat Bot")

img = PhotoImage(file="C:\\Users\\AtulPR007\\Desktop\\Python Proj\\bott.png")

photoL = Label(main, image=img)
photoL.pack(pady = 5)

# take query : it takes audio as input from user and converts it into string

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Bot is listening, try to speak...")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language ='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Not Recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msg.insert(END,"you :" + query)
    msg.insert(END,"bot :" + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msg.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msg = Listbox(frame, width = 60, height = 15, yscrollcommand = sc.set)

sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=5)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 18))
textF.pack(fill=X, pady=8)

btn = Button(main, text="Ask from My Bot", font=("Verdana",18), command = ask_from_bot)
btn.pack()

# creating a function
def enter_func(event):
    btn.invoke()

# going to bind main window with bind key

main.bind('<Return>',enter_func)

def repeat():
    while True:
        takeQuery()

t = threading.Thread(target = repeat)

t.start()

main.mainloop()