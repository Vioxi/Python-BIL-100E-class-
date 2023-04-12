import tkinter
top = tkinter.Tk()
top.mainloop()

from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, textvariable = var, relief = RAISED)
var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()

import tkinter
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def hello():
    messagebox.showinfo("Say hello", "Hello Python")
B1 = Button (top, text = "Say hello", command = hello)
B1.place(x = 35, y = 50)
top.mainloop()

##CheckButton

import tkinter
top = Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton (top, text = "Music", variable = CheckVar1, \
                  onvalue = 1, offvalue = 0, height = 5, width = 20)

C2 = Checkbutton (top, text = "Video", variable = CheckVar2, \
                  onvalue = 1, offvalue = 0, height = 5, width = 20)

C1.pack()
C2.pack()
top.mainloop()


##Radiobutton

import tkinter
window=tkinter.Tk()

window.geometry("150x50+600+250")
var=tkinter.IntVar()
var.set(1)

Radiobutton1=tkinter.Radiobutton(window,
                                 text="1. radio button",
                                 variable=var,
                                 value=1)
Radiobutton1.pack()

Radiobutton2=tkinter.Radiobutton(window,
                                 text="2. radio button",
                                 variable=var,
                                 value=2)
Radiobutton2.pack()

window.mainloop()

###Ekstra Radiobutton
import tkinter
def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)
    
root = Tk()
var = IntVar()
R1= Radiobutton(root, text = "Option 1", variable = var, value = 1,
                command = sel)
R1.pack( anchor = W )

R2= Radiobutton(root, text = "Option 2", variable = var, value = 2,
                command = sel)
R2.pack( anchor = W )

label = Label(root)
label.pack()
root.mainloop()

##Menu

from tkinter import *
import tkinter

top = Tk()

mb = Menubutton (top, text = "condiments", relief = RAISED)
mb.grid()
mb.menu = Menu (mb, tearoff = 0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton (label = "mayo",
                         variable=mayoVar)
mb.menu.add_checkbutton (label = "ketchup",
                         variable=ketchVar)

mb.pack()
top.mainloop()
