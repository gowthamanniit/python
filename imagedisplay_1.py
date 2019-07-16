from tkinter import *

window=Tk()
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
window.configure(bg="green",width=w,height=h)


canvas=Canvas(window,width=500,height=600,bg="red")
canvas.pack() # important
img=PhotoImage(file="123.ppm")   # only support PhontoImage class: GIF,PPM & PGM.

canvas.create_image(20,20,anchor=NW,image=img)

window.mainloop()
