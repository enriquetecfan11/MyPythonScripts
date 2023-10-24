import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "admin",
    passwd = "mondejar"
    database="floristeria"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM floristeria")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)