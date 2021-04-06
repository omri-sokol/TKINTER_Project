from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Title")
root.iconbitmap("icon.png")

# How big we want a window to be
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+ "x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()

btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()

