from tkinter import messagebox
import tkinter
import os
window=tkinter.Tk()
wi=window.winfo_screenwidth()
he=window.winfo_screenheight()
window.configure(width=wi,height=he,bg="green")

def display():
    data=untb.get()        # get information
    restb.delete(0,"end")  # clear textbox
    data=data.upper()
    restb.insert(0,data)   # insert data
    reslbl.configure(text=data) # how to store data in label
    window.destroy()
    os.system("gui_05.py")
    #messagebox.showinfo("Success","Your Name :"+data)
    #messagebox.showwarning("hai","warning message")
    #messagebox.showerror("error","failure")

unlbl=tkinter.Label(window,text="Enter Text:")
unlbl.place(x=200,y=200)
untb=tkinter.Entry(window)
untb.place(x=300,y=200)

reslbl=tkinter.Label(window,text="Upper Case:")
reslbl.place(x=200,y=400)
restb=tkinter.Entry(window)
restb.place(x=300,y=400)

  
but1=tkinter.Button(window,text="clickme",command=display)
but1.place(x=300,y=300)

window.mainloop()
