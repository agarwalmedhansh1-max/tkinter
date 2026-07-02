from tkinter import *

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

def check_password():
    password = entry.get()
    length = len(password)
    if length == 0:
        result.config(text="Please enter a password.", fg="red")
    elif length < 6:
        result.config(text="Weak Password", fg="red")
    elif length < 10:
        result.config(text="Medium Password", fg="orange")
    else:
        result.config(text="Strong Password", fg="green")


title = Label(root, text="Password Strength Checker",bg="lightblue")
title.pack()

label = Label(root, text="Enter Password:",bg="lightblue")
label.pack()

entry = Entry(root, show="*", width=30)
entry.pack()

button = Button(root,text="Check Strength",command=check_password,bg="yellow")
button.pack()

result = Label(root,text="",bg="lightblue")
result.pack()

root.mainloop()