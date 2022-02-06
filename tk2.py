from tkinter import *

root = Tk()# Creating a window

ttl = root.title("Tkinter introduction") #Adding a title
lbl = Label(text="YASEMIN AY") #Creating a label
lbl.pack() #If we do not pack,the label cannot be seen.

root.mainloop()
