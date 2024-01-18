import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="05122004tim",
  database="mydb"
)

mydatabase = mydb.cursor()


mydatabase.execute("SELECT * FROM user;")
result = mydatabase.fetchall()

print(result)