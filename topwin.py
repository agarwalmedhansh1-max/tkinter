from tkinter import *

root= Tk()
root.title("Top window")
root.geometry("500x500")

r=Label(text="This is root Window", fg= 'black')

def topwin():
    top=Toplevel()
    top.title("This is top window")
    top.geometry("180x180")

    t=Label(text="This is top window", fg ='black')
    t.pack()

btn=Button(text="Click to go to another window", command=topwin, fg= 'black', bg='yellow')

r.pack()
btn.pack()

root.mainloop()
