from tkinter import *

window = Tk()
window.title("sample window")
window.geometry("400x300")
def handle_keypress(event):
    """Print the character
    associated to the key
    pressed"""
    if event.char=="L":
        print(event.char)
    if event.char=="g":
            print("get good")
    if event.char=="f":
            print("fall")
def handle_click(event):
    event.char
    print("the button was clicked")
button=Button(text="click me")
button.pack()
button.bind("<Button-1>",handle_click)

# Bind keypress event to
# handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()
