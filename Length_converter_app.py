from tkinter import *
window=Tk()
window.title("sample window")
window.geometry("400x300")
lbl=Label(text="inches to centimeters",fg="white",bg="#072F5F",height=1,width=300)
name_lbl=Label(text="inches",bg="#3895D3")
number_entry=Entry()
def display():
    name=int(number_entry.get())*2.54
    global Message
    text_box.insert(END,name)
number_entry2=Entry()
text_box=Text(height=1)
bnt=Button(text="confirm",command=display,height=1,bg="#1261A0",fg="white")
lbl2=Label(text="centimeters",height=1,bg="#1261A0")
lbl.pack()
name_lbl.pack()
number_entry.pack()
bnt.pack()
lbl2.pack()
text_box.pack()
window.mainloop()
