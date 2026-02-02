from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("")

#Set size of window
root.geometry("1000x400")

msgbox = Text(root)

def savefile():
	with open('demo.txt', 'w') as f:
		f.write('Updated text')
	


# Create buttons
save_button = Button(root,text='Save',background="lightgreen")
openfile_button = Button(root,text='Open File')
newfile_button = Button(root,text='New File', command=savefile)


# Place widgets in window (with pack function!)
save_button.place(x=0, y=0, anchor = NW)
openfile_button.place(x=95,y=0, anchor = NW)
newfile_button.place(x=195,y=0,anchor= NW)
msgbox.place(x=0,y=30, anchor=NW)


# Start the GUI event loop
root.mainloop()
