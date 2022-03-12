import tkinter
import tkinter.ttk as tv
window=tkinter.Tk()
wi=window.winfo_screenwidth()
he=window.winfo_screenheight()
window.configure(width=wi,height=he,bg="blue")
treeview=tv.Treeview(window)

treeview['column']=('Roll number','Student Name','Mark')
treeview.column('#0',width=0,stretch="No")

treeview.column('Roll number',width=100)
treeview.column('Student Name',width=100)
treeview.column('Mark',width=100)

treeview.heading('Roll number',text="Register Number")
treeview.heading('Student Name',text="Student Name")
treeview.heading('Mark',text="Mark")

treeview.insert(index=0,values=('1001','gowthaman','99'))
treeview.insert(parent="",index=1,values=('1001','gowthaman','99'))
treeview.place(x=100,y=100)



window.mainloop()
