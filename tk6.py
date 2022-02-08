from tkinter import *
root = Tk()
root.geometry("1000x1000")
headline=root.title("XOX TABLE")

Label(text="LABEL WIDGET",font="25",pady=10).grid(row=0,column=0,columnspan=4)

lbl1=Label(text="X",width="20",height="10",bg="red",font="bold")
lbl1.grid(row=1,column=0)

lbl2=Label(text="X",width="20",height="10",bg="yellow",font="bold")
lbl2.grid(row=1,column=1)

lbl3=Label(text="O",width="20",height="10",bg="orange",font="bold")
lbl3.grid(row=1,column=2)

lbl4=Label(text="O",width="20",height="10",bg="green",font="bold")
lbl4.grid(row=2,column=0)

lbl5=Label(text="X",width="20",height="10",bg="blue",font="bold")
lbl5.grid(row=2,column=1)

lbl6=Label(text="O",width="20",height="10",bg="purple",font="bold")
lbl6.grid(row=2,column=2)

lbl7=Label(text="X",width="20",height="10",bg="pink",font="bold")
lbl7.grid(row=3,column=0)

lbl8=Label(text="X",width="20",height="10",bg="brown",font="bold")
lbl8.grid(row=3,column=1)

lbl9=Label(text="X",width="20",height="10",bg="maroon",font="bold")
lbl9.grid(row=3,column=2)

root.mainloop()
 
