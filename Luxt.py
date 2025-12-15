from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("500x200")

msgbox = Text(root, height = 5, width = 30)

# Create buttons
red_button = Button(root,text='Save')

#Add a label
label = Label(root, text=" What color is the light")


# Place widgets in window (with pack function!)
red_button.grid(row=0,column=0)
msgbox.grid(row=1,column=0)

# Start the GUI event loop
root.mainloop()
