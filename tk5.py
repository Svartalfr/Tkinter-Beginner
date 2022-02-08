from tkinter import *

root=Tk()
root.geometry("350x350+100+100")

headLine=root.title("Grid System")
#Griding is a coordinating system
"""
txt=Label(root,text="Hello World")
txt2=Label(root,text="Hello Moon")
txt.pack() #packing is working with default coordinate
txt2.pack() #that's why our label widget is in the middle
"""


txt=Label(root,text="Hello World")
txt2=Label(root,text="Hello Moon")

txt.grid(row=0,column=0)# Now we coordinated txt 0,0 and its coordinate will never change.
txt2.grid(row=1,column=1)



root.mainloop()
