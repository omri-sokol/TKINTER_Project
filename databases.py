from tkinter import *
from PIL import ImageTk,Image
import sqlite3

# sqlite 5 datatypes: text, integers (whole #s), real (decimal #s),
# null (does it exist or not), blob (image files, videos files)

root = Tk()
root.title("Title")
root.iconbitmap("icon.png")
root.geometry("400x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")




# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()



