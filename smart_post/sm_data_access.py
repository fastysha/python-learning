from sm_dbconnector import db
mycursor = db.cursor()
mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



