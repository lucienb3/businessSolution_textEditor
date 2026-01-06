from tkinter import *
#need to install on all machines
from tkmacosx import Button

root = Tk()
root.title("Updating Labels")

#Set size of window
#root.geometry("300x200")

button1 = Button(root, text='Button1!')
button2 = Button(root, text='Button2!')
button3 = Button(root, text='Button3!')
rndbutton = Button(root, text='Random Button!')

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