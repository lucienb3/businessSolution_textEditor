from tkinter import *
#need to install on all machines
from tkmacosx import Button

import random


root = Tk()
root.title("Updating Labels")

#Set size of window
#root.geometry("300x200")





def update1():
	label1.config(text = 'Updated 1!')

def update2():
	label2.config(text = 'Updated 2!')

def update3():
	label3.config(text = 'Updated 3!')


def random1():
	choices = [button1, button2, button3, label1, label2, label3]
	num = random.randint(0, 5)
	choices[num].config(text='RANDOMLY PICKED!')






button1 = Button(root, text='Button1!', command=update1)
button2 = Button(root, text='Button2!', command=update2)
button3 = Button(root, text='Button3!', command=update3)
rndbutton = Button(root, text='Random Button!', command=random1)

label1 = Label(root, text='Label 1')
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')






button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)
rndbutton.grid(row=3,column=1)
label1.grid(row=0,column=2)
label2.grid(row=1,column=2)
label3.grid(row=2,column=2)


root.mainloop()