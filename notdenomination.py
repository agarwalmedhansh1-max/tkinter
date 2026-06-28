from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("Denominations")
root.geometry("500x500")

def alert():
    msg=messagebox.showinfo("Alert", "Click ok to continue")
    if msg=="ok":
        topwin()        

btn=Button(text="Click here to get started", command=alert, fg='black', bg='yellow')

def topwin():
    top=Toplevel()
    top.title("Denomination calculator")
    top.geometry("400x400")

    d=Label(topwin, "Write the amount: ", bg="#0A8510B0")
    d1=Entry(topwin)

    d.place(x=20, y= 15)
    d1.place(x=20,  y=35)

    btn2=Button(topwin, text="Calculate", command=cal, bg="#0A8510B0")
    btn2.place(x=35, y=55)

    textbox=Text(master=topwin, height=10)
    textbox.place(x=100, y=200 )

    def cal():
        global amount
        amount=int(d1.get())
        note1=amount//2000
        note2=(amount%2000)//500
        note3=((amount%2000)%500)//100
        note4=(((amount%2000)%500)%100)//50

        note1text="2000 denominations are: " + str(note1) + '\n'
        note2text="500 denominations are: " + str(note2) + '\n'
        note3text="100 denomiantions are: " + str(note3) + '\n'
        note4text="50 denomiantions are; " + str(note4)+ '\n'

        textbox.insert(END, note1text)
        textbox.insert(END, note2text)
        textbox.insert(END, note3text)
        textbox.insert(END, note4text)
    topwin.mainloop()
    
btn.pack()

root.mainloop()