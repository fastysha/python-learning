from unicodedata import name
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

def find_user_by_phone_number(phone_number):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE UserPhoneNumber = %s", (phone_number,))
    user = cursor.fetchone()
    # print(f'Finded user by phone {phone_number} is: {user}')
    return user

def create_user(new_user):
    cursor = db.cursor()
    sql = "INSERT INTO Users (UserName, UserSurname,UserPhoneNumber,Country) VALUES (%s, %s,%s,%s)"
    args = (new_user["name"],new_user["surname"],new_user["phone_num"],new_user["country"])
    cursor.execute(sql, args)
    db.commit()
    print(cursor.rowcount, "record inserted.")
