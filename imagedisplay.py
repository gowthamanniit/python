from tkinter import *
from PIL import Image,ImageTk

    # must install : pip install pillow
    #C:\Users\niit\AppData\Local\Programs\Python\Python37-32\Scripts
    # cmd --> pip install pillow

window=Tk()
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
window.configure(bg="green",width=w,height=h)

load=Image.open("123.jpg")
render=ImageTk.PhotoImage(load)

l1=Label(window,image=render)
# l1.image=render # no need
l1.place(x="0",y="0")


window.mainloop()
