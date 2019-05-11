import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1234")

mycur=mydb.cursor()

mycur.execute("drop database karthick")
