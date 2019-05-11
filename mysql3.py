import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="karthick")

mycursor=mydb.cursor()

mycursor.execute("insert into test1(sname) values ('gowthaman')")
mydb.commit()
mycursor.close()
mydb.close()
