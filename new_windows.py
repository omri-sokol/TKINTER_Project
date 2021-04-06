from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Title")
root.iconbitmap("icon.png")

def open():
    global img
    top = Toplevel()
    # lbl = Label(top, text="Hello").pack()
    img = ImageTk.PhotoImage(Image.open("icon.png"))
    label = Label(top, image=img).pack()
    top.title("Anything")
    top.iconbitmap("icon.png")
    btn2 = Button(top, text="close window", command=top.destroy).pack()
    

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()

