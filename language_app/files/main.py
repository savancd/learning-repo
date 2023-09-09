from tkinter import *

root = Tk()

#	Creating a Label Widget
myLabel1 = Label(root, text="Tagalog - Serbian Language App")
myLabel2 = Label(root, text="Made by: ")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
