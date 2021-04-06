from tkinter import *

root = Tk()

# When calling functions watch out for paranthesis

# In Entry constructor:
#     width = #
#     borderwidth = #
#     fg and bg same as button constructor

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")
# e.get() gets what you type in to the text box

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick, fg = "purple")
myButton.pack()

root.mainloop()
