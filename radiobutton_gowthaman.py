import mysql.connector
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("this is title")
window.configure(bg="green",width="555",height="666")
wi=window.winfo_screenwidth()
hi=window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(wi,hi))

#method : 1
rb=StringVar()
rb.set("Male") # default male selected


male=Radiobutton(window,text="male",value="Male",variable=rb)
male.place(x=100,y=200)

female=Radiobutton(window,text="female",value="feMale",variable=rb)
female.place(x=100,y=250)

others=Radiobutton(window,text="others",value="others",variable=rb)
others.place(x=100,y=300)


#method : 2

r=IntVar()
r.set(1)  # default male selected

m=Radiobutton(window,text="male",value=1,variable=r)
m.place(x=400,y=200)

f=Radiobutton(window,text="female",value=2,variable=r)
f.place(x=400,y=250)

o=Radiobutton(window,text="others",value=3,variable=r)
o.place(x=400,y=300)


# get selected value

def fun():
    print("hai you selected ",r.get(),rb.get())

b=Button(window,text="selected male or female or others",command=fun)
b.place(x=150,y=400)



window.mainloop()
