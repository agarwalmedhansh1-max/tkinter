from tkinter import *

root = Tk()
root.title("Calculate your interest: ")
root.geometry("500x500")

principal=Label(text='Enter principal amount: ', fg='black', bg='white')
p=Entry()

time=Label(text='Enter Duration: ', fg='black', bg='white')
t=Entry()

rate=Label(text="Enter rate of interest: " , fg = 'black', bg = 'white')
r=Entry()

def display():
    p1=p.get()
    t1=t.get()
    r1=r.get()

    compund=(int(p1) * ((1 + (int(r1)/100)))**int(t1)) - int(p1)
    compundtext= "The compund interest is:  " + str(compund ) + ' \n'

    simple= (int(p1) * int(t1) * int(r1)) / 100
    simpletext = "The simple interest is: " + str(simple) + '\n'
    textbox.insert(END, compundtext)
    textbox.insert(END, simpletext)

textbox=Text(height=8)
btn=Button(text='Product', command=display, height=1, bg='yellow', fg='black')

principal.pack()
p.pack()

time.pack()
t.pack()

rate.pack()
r.pack()

textbox.pack()
btn.pack()

root.mainloop()



