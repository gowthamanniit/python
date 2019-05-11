import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="karthick")

    mycursor=mydb.cursor()

    rno=int(input("Enter student rollnumber:"))
    name=input("Enter student name:")
    mark=int(input("Enter student mark:"))

    mycursor.execute("insert student values(%d,'%s',%d)"%(rno,name,mark))
    mydb.commit()
    print("successfully inserted into database")
    mycursor.close()
    mydb.close()
except:
    print("error" , sys.exc_info()[0])

finally:
    print("program finished")
