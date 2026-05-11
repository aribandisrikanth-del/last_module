from tkinter import *
window=Tk()
window.title("password")
window.geometry("800x600")
lbl=Label(text="hello",fg="white",bg="#072F5F",height=1,width=300)
name_lbl=Label(text="full name",bg="#3895D3")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message="welcome to application"
    greet=" hello "+name+"\n"
    message2=" what is your password to login "
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,message2)
def display2():
    name=name_entry.get()
    global Message
    log_in="\n welcome "+name+"\n"
    text_box.insert(END,log_in)
text_box=Text(height=3)
bnt=Button(text="Begin",command=display,height=1,bg="#1261A0",fg="white")
bnt2=Button(text="confirm",command=display2,height=4,bg="#1261A0",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
bnt.pack()
text_box.pack()
bnt2.pack()
window.mainloop()