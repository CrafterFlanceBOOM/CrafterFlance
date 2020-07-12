from tkinter import *
import time as t
import sys as program
from tkinter import messagebox
from tkinter.messagebox import *
root = Tk()
def tnt():
    root.configure(bg="white")
    t.sleep(2)
    canvas.destroy()
    t.sleep(0.3)
    oof()
def mover():
    w = Scale(root, from_=0, to=42) 
    w.pack()
def oof():
    showinfo("Unkown Cave","You died! Reseting map...")
    t.sleep(6)
    showinfo("ERROR","Reset the game\reload the game")
    program.exit()
    
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='Items', menu=filemenu) 
filemenu.add_command(label='Mover',command=mover) 
filemenu.add_command(label='TNT',command=tnt) 
filemenu.add_separator()
 
canvas = Canvas(root, width=436, height=642)
canvas.pack()
img = PhotoImage(file="Character.png")
image = canvas.create_image(10, 10, anchor=NW, image=img)
root.className = "Unknown Cave"
root.configure(bg='brown')
def move(event):
    if event.char == "a":
        canvas.move(image, -10, 0)
    elif event.char == "d":
        canvas.move(image, 10, 0)
    elif event.char == "w":
        canvas.move(image, 0, -10)
    elif event.char == "s":
        canvas.move(image, 0, 10)
    elif event.char == "g":
        ca = Canvas(root, width=436, height=642)
        ca.pack()
        cl = PhotoImage(file="Brix.png")
        clone = ca.create_image(10, 10, anchor=NW, image=cl)
        
        
root.bind("<Key>", move)
root.mainloop()