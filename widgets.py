from tkinter import *
from datetime import date

win=Tk()

win.title('widgets for starters')
win.geometry('500x500')

lb1= Label(text='Hey there', fg='black', bg='white', height='1', width='10')
name_lb1=Label(text='Enter your name', fg='black', bg='white')
name_entry=Entry()

def display():
    name=name_entry.get()

    global message

    message='Welcome to the application!.\n Todays date is: '
    greet='Hello ' + name + ' \n'
    text_box.insert(END , greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box=Text(height=20)
btn=Button(text='Begin', command=display, height=1, bg='yellow', fg='black')

lb1.pack()
name_lb1.pack()
name_entry.pack()
text_box.pack()
btn.pack()

win.mainloop()

