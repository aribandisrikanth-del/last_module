from tkinter import *
root = Tk()
root.geometry("200x300")
root.title("main")
l = Label(root, text = "This is root window")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
l=Label(root,text="this is root window")
btn=Button(root,text="click here to open another window",command=topwin)
l.pack()
btn.pack()
root.mainloop()