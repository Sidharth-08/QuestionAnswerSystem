
from Tkinter import *
import tkMessageBox

# Code to add widgets will go here...
root = Tk()




frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

#Vertical (y) Scroll Bar
yscrollbar = Scrollbar(frame)
yscrollbar.pack(side=RIGHT, fill=Y)


var = StringVar()
query = StringVar()
label = Message( frame, textvariable=var, relief=RAISED )


L2 = Label(frame, text="Corpus")
L2.pack( side = TOP)
text = Text(frame,yscrollcommand=yscrollbar.set)
text.pack(side=TOP)
yscrollbar.config(command=text.yview)


L1 = Label(frame, text="Query")
L1.pack( side = LEFT)
E1 = Text(frame, bd =5,yscrollcommand=yscrollbar.set,width=70,height=4)
E1.pack(side = LEFT)
yscrollbar.config(command=text.yview)


def helloCallBack():
	query=E1.get(1.0,END)[:-1]
   	tkMessageBox.showinfo( str(query), "Answer")
B = Button(bottomframe, text ="Submit", command = helloCallBack)
B.pack(side=BOTTOM)






root.mainloop()