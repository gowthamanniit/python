import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="karthick")

mycursor=mydb.cursor()

mycursor.execute("insert into student(rno,mark) values (1003,78)")
mydb.commit()
mycursor.close()
mydb.close()
