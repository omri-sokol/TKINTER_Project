from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Game")
icon = input("Enter a .png to establish as your icon for the game: ")
root.iconbitmap(icon)
root.geometry("1600x800")

# Create a database or connect to one
conn = sqlite3.connect('scores.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE scores (
        name text,
        score integer
        )""")
'''

def exit_button():
    root.destroy()

def summary(score):
    global window5
    window5 = Toplevel()
    window5.title("Summary")
    window5.iconbitmap(icon)
    window5.geometry("1600x800")
    
    Label(window5, text='''This is a summary of your game.\n You scored ''' + str(score) + ''' out of 6 possible points!\n
    Additionally, you played a popups game!\n Thank you for playing! Click the 'exit' button to exit the game.''').pack()
    
    Button(window5, text="exit", command=exit_button).pack()

def popup1():
    messagebox.showinfo("Popup", "This informative popup is here to tell you to have a good day")
    
def popup2():
    messagebox.showwarning("Popup", "This warning is here to tell you to be aware of bad people")

def popup3():
    response = messagebox.askyesno("Popup", "Are you feeling good today?")

def popup4():
    response = messagebox.askokcancel("Popup", "Glad you clicked through these buttons!")

def level2(score, result1, result2, result3, result4, result5, result6):
    global window4
    window4 = Toplevel()
    window4.title("Level 2")
    window4.iconbitmap(icon)
    window4.geometry("1600x800")
    
    if result1 == 20:
        score += 1
    if result2 == "Sacremento":
        score +=1
    if result3 == "Not Portland":
        score +=1
    if result4 == "Los Angeles":
        score +=1
    if result5 == "San Francisco":
        score +=1
    if result6 == "Lebron James":
        score += 1
    
    level_label = Label(window4, text="Click through the buttons to play with some popups")
    level_label.pack()
    
    
    Button(window4, text="Button 1", command=popup1).pack()
    Button(window4, text="Button 2", command=popup2).pack()
    Button(window4, text="Button 3", command=popup3).pack()
    Button(window4, text="Button 4", command=popup4).pack()
    
    Label(window4, text="You have completed the level. Click 'next' to continue.", pady=30).pack()
    
    Button(window4, text="next", command=lambda: summary(score)).pack()

def level1():
    global window3
    window3 = Toplevel()
    window3.title("Level 1")
    window3.iconbitmap(icon)
    window3.geometry("1600x800")
    
    question1 = Label(window3, text="What is 10 + 10?")
    question1.pack()
    
    OPTIONS = [
        ("5", 5),
        ("-316", -316),
        ("20", 20),
        ("3", 3)
        ]
    
    result1 = IntVar()
    
    for text, answer in OPTIONS:
        Radiobutton(window3, text=text, variable=result1, value=answer).pack()
    
    question2 = Label(window3, text="Check all the boxes that are cities in California")
    question2.pack(pady=20)
    
    check1 = StringVar()
    check2 = StringVar()
    check3 = StringVar()
    check4 = StringVar()
    
    checkbox1 = Checkbutton(window3, text="Sacremento", variable=check1, onvalue="Sacremento", offvalue="Not Sacremento")
    checkbox1.deselect()
    checkbox1.pack()
    checkbox2 = Checkbutton(window3, text="Portland", variable=check2, onvalue="Portland", offvalue="Not Portland")
    checkbox2.deselect()
    checkbox2.pack()
    checkbox3 = Checkbutton(window3, text="Los Angeles", variable=check3, onvalue="Los Angeles", offvalue="Not Los Angeles")
    checkbox3.deselect()
    checkbox3.pack()
    checkbox4 = Checkbutton(window3, text="San Francisco", variable=check4, onvalue="San Francisco", offvalue="Not San Francsico")
    checkbox4.deselect()
    checkbox4.pack()
        
    question3 = Label(window3, text="Who is the greatest basketball player of all time?")
    question3.pack(pady=20)
    
    players = [
        "Michael Jordan",
        "Lebron James",
        "Brian Scalabrine",
    ]
    
    clicked = StringVar()
    clicked.set(players[0])
    
    drop = OptionMenu(window3, clicked, *players)
    drop.pack(pady=20)
        
    next_level_button = Button(window3, text="Next Level", command=lambda: level2(0, result1.get(), check1.get(), check2.get(), check3.get(), check4.get(), clicked.get()))
    next_level_button.pack()


def add_to_database():
    # Create a database or connect to one
    conn = sqlite3.connect('scores.db')

    # Create cursor
    c = conn.cursor()
    
    # Insert Into Table
    c.execute("INSERT INTO scores VALUES (:name, :score)",
              {
                 'name': f_name.get(),
                 'score': 0
              })
    
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    
    global window2
    window2 = Toplevel()
    window2.title("Purpose")
    window2.iconbitmap(icon)
    window2.geometry("1600x800")
    game_explanation_label = Label(window2, text='''
    There are two levels to the game.\n
    The purpose of the first level is to test your intelligence.\n
    The purpose of the second level is to play with popups.\n
    Click the “Start Game” button to begin.
    ''')
    game_explanation_label.pack()
    
    start_game_button = Button(window2, text="Start Game", command=level1)
    start_game_button.pack(pady=20)
    
    
    
    

enter_name_label = Label(root, text="Enter your name:")
enter_name_label.pack()

f_name = Entry(root, width=30)
f_name.pack(pady=20)

database_button = Button(root, text="Add your name to the database", command=add_to_database)
database_button.pack(pady=20)


# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop