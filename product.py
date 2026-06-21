from tkinter import *

root = Tk()
root.title("Product")
root.geometry("500x500")

num1 = Label(text='Enter a number', fg='black', bg='white')
ne=Entry()

num2= Label(text='Enter another number', fg='black', bg='white')
n2e=Entry()

def display():
    n1=ne.get()
    n2=n2e.get()

    product= int(n1)* int(n2)
    textbox.insert(END, product)

textbox=Text(height=10)
btn=Button(text='Product', command=display, height=1, bg='yellow', fg='black')

num1.pack()
ne.pack()
num2.pack()
n2e.pack()
textbox.pack()
btn.pack()

root.mainloop()
