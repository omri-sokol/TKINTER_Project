from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Title")
root.iconbitmap("icon.png")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

def open():
    # don't forget globals
    global img
    root.filename = filedialog.askopenfilename(initialdir="/omrisokol/TKINTER", title="Select a File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image=img).pack()

c = Checkbutton(root, text="Check here", variable=var, onvalue=open, offvalue="James")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()


