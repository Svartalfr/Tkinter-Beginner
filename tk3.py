from tkinter import *
root= Tk()

root.geometry("400x500+0+0") # We can 

ttl = root.title("Colouring") #Adding title


lbl = Label(text="THIS IS RED",fg="red")#Creating a label and coloring the label. ***fg comes from foreground***
lbl.pack()#If we do not pack,the label will not be visible.
#Event loop
root.mainloop()

