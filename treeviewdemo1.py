import tkinter
import tkinter.ttk as tv
window=tkinter.Tk()
wi=window.winfo_screenwidth()
he=window.winfo_screenheight()
window.configure(width=wi,height=he,bg="blue")


import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="ds")
cur=con.cursor()
cur.execute("select * from score1")
alldata=cur.fetchall()

    
treeview=tv.Treeview(window)



#treeview['column']=('Roll number','Student Name','Mark')
treeview['column']=cur.column_names

treeview.column('#0',width=0,stretch="No")

for cn in cur.column_names:
    treeview.column(cn,width=100)
    treeview.heading(cn,text=cn)
    
#treeview.column('Roll number',width=100)
#treeview.column('Student Name',width=100)
#treeview.column('Mark',width=100)

#treeview.heading('Roll number',text="Register Number")
#treeview.heading('Student Name',text="Student Name")
#treeview.heading('Mark',text="Mark")
k=1
for data in alldata:
        k+=1
        treeview.insert(parent="",index=k,values=data)
#treeview.insert(parent="",index=0,values=('1001','gowthaman','99'))
#treeview.insert(parent="",index=1,values=('1001','gowthaman','99'))
treeview.place(x=100,y=100)

window.mainloop()
