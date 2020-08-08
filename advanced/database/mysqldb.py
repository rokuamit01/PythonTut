import mysql.connector

db = mysql.connector.connect(host="localhost", user="automation", passwd="automation", database="python")

print("########################")
cursor = db.cursor()
cursor.execute("show databases")
for i in cursor:
    print(i)

print("########################")
cursor.execute("select * from student")
for i in cursor:
    print(i)

print("########################")
cursor.execute("select * from student")
result = cursor.fetchone()
print(result)
print("########################")
result = cursor.fetchall()
print(result)

print("########################")
cursor.execute("show databases")
result = cursor.fetchall()
print(result)
