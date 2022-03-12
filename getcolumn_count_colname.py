import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="12345",database="ds")
cur=con.cursor()
cur.execute("select * from score1")

alldata=cur.fetchall()

# find no. of columns
print("No. of columns : ",cur.column_names)
print("No. of columns : ",len(cur.column_names))
for cn in cur.column_names:
    print(cn)
# find no.of rows
print("No. of rows :",len(alldata))
#showing all rows
for r in  alldata:
    print(r)
