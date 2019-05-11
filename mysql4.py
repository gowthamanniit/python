import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="karthick")

    mycursor=mydb.cursor()


    mycursor.execute("insert student values(1111,'jjj',89)")
    mydb.commit()
    print("successfully inserted into database")
    mycursor.close()
    mydb.close()
except:
    print("error" , sys.exc_info()[0])

finally:
    print("program finished")
