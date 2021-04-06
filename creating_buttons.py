from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Button Clicked!")
    myLabel.pack()
    
# In Button constructor:
#     state = DISABLED -> disables the button
#     padx and pady = something -> is the size of the square button
#     command = function -> calls a function when button is clicked. remember no paranthesis!
#     fg = color as a string -> colors the text of the button
#     bg = color as a string -> background of button gets colored

myButton = Button(root, text="Click Me!", command=myClick, fg = "purple")
myButton.pack()

root.mainloop()