from tkinter import *

window = Tk()
window.title("login screen") # Added quotes
window.geometry("400x300")  # Added quotes

frame = Frame(master=window, height=200, width=360, bg="#d0efff") # Fixed typo 'wisth'

lbl = Label(text="hello", fg="white", bg="#072F5F", height=1, width=300) # Added quotes
name_lbl = Label(text="full name", bg="#3895D3") # Added quotes
name_entry = Entry()
def display():
    # Fixed global assignment and string formatting
    name = name_entry.get()
    message = "\nwelcome to application"
    greet = "hello " + name + " "
    text_box.insert(END, greet)
    text_box.insert(END, message)

def display2():
    name = name_entry.get()
    # Fixed global assignment and string formatting
    log_in = "\nwelcome " + name + "\n"
    text_box.insert(END, log_in)

def display3():
    # pass_entry is created locally in the original, we define it on the window instead of trying to pack inside the Text widget
    pass_entry.place(x=20, y=140)
    join="you have succesfuly logged in"
    text_box.insert(END,join)

# Create the password entry here so display3 can just place it, and it can be accessed
pass_entry = Entry(frame, show="*")

text_box = Text(frame, height=3) # Changed master to frame to keep it organized

bnt = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white") # Added quotes
bnt2 = Button(text="confirm", command=display2, height=4, bg="#1261A0", fg="white") # Added quotes
bnt3 = Button(text="password", command=display3, height=1, bg="#1261A0", fg="white") # Added quotes

# Layout management
frame.pack()
lbl.pack()
name_lbl.pack()
name_entry.place(x=20,y=140)
bnt.pack()
text_box.pack()
bnt2.pack()
bnt3.pack() # Added missing button 3 to the UI

window.mainloop()
