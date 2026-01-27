from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("")

#Set size of window
root.geometry("1000x400")

def newfile():
	with open('demo.txt', 'w') as f:
		f.write('Updated text')
	print(msgbox.get('1.0',END))

msgbox = Text(root)

# Create buttons
save_button = Button(root,text='Save',background="lightgreen")
openfile_button = Button(root,text='Open File')
newfile_button = Button(root,text='New File', command=newfile)


# Place widgets in window (with pack function!)
save_button.place(x=0, y=0, anchor = NW)
openfile_button.place(x=95,y=0, anchor = NW)
newfile_button.place(x=195,y=0,anchor= NW)
msgbox.place(x=0,y=30, anchor=NW)


# Start the GUI event loop
root.mainloop()
