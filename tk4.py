from tkinter import * # use tkinter modul

root = Tk() #we called modul as root

#basic settings
root.geometry("700x600+0+0") #700 = width,600 = height,0,0 => starting point

root.title("YASEMIN")#Page title
root.config(bg="red")
root.resizable(False,False)

#label widgets

lbl=Label() #create an object
lbl["text"]= "Yasemin AY Yasemin AY Yasemin AY" # give a value to the object
lbl["bg"]="yellow" #backgroud
lbl["fg"]="blue" #font colour
lbl["font"]= "Ariel 12" # font type and font size
lbl["cursor"]="exchange" # we can change the cursor
lbl["padx"]=20           #up space
lbl["pady"]=20
lbl["width"]=30         #character change
lbl["wraplength"]=100   #determines when a label's text should be wrapped into multiple lines
lbl.pack() #make the label visible

root.mainloop()# make the window permanent 
