from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Strength Checker App")
window.geometry("400x350")
window.configure(bg="#f0f0f0")

# Label and Entry for password
name_lbl = Label(text="Enter Password:", bg="#3895D3", fg="white", font=("Arial", 10, "bold"))
password_entry = Entry(window, show="*", font=("Arial", 12)) # 'show' masks the password

def check_strength():
    password = password_entry.get()
    
    # Validation checks
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    # Strength evaluation
    if length == 0:
        strength_text = "Please enter a password."
        color = "black"
    elif length < 6:
        strength_text = "Very Weak (Too short)"
        color = "red"
    elif length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength_text = "Strong (Excellent variety)"
        color = "green"
    elif length >= 6 and (has_upper + has_lower + has_digit) >= 2:
        strength_text = "Medium (Consider adding symbols)"
        color = "orange"
    else:
        strength_text = "Weak (Needs numbers/letters)"
        color = "red"

    # Update the text box with results
    text_box.delete(1.0, END) # Clear previous text
    text_box.insert(END, f"Strength: {strength_text}")
    text_box.tag_config("result", foreground=color, font=("Arial", 10, "bold"))
    text_box.tag_add("result", 1.0, END)

# UI Elements
name_lbl.pack(pady=(20, 5))
password_entry.pack(pady=5)

bnt = Button(text="Check Strength", command=check_strength, height=1, bg="#1261A0", fg="white", font=("Arial", 10, "bold"))
bnt.pack(pady=15)

# Text box to display result
text_box = Text(window, height=3, width=40, font=("Arial", 10), bg="#e6e6e6")
text_box.pack(pady=5)

window.mainloop()

