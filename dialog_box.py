from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

# This file is for opening files from finder,
# but remember it only gives the files location, so you have to
# open the actual file after you have found the location.

root = Tk()
root.title("Title")
root.iconbitmap("icon.png")


def open():
    # don't forget globals
    global img
    root.filename = filedialog.askopenfilename(initialdir="/omrisokol/TKINTER", title="Select a File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(image=img).pack()
    
btn = Button(root, text="Open File", command=open).pack()

root.mainloop()


