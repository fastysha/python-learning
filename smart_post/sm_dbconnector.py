from sm_data_models import ParcelStatus
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

############################################
############# Users Table SQL ##############
# ########################################## 
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


############################################
############# Parcels Table SQL ############
# ##########################################     
def find_all_not_delivered_parcels() -> list:
    cursor = db.cursor(dictianory=True)
    sql = "SELECT * FROM Parcels WHERE Status = %s AND todo records those live for more than 3 minutes "
    cursor.execute(sql, (ParcelStatus.IN_PROGRESS.name, ))
    parcels = cursor.fetchall()
    return parcels


def update_parcels(status: str, delivery_time_seconds: int, parcel_ids: list):
    cursor = db.cursor()
    sql = "UPDATE Parcels SET Status = %s, DeliveryDate >= (CURRENT_TIMESTAMP() - INTERVAL %s SECONDS) WHERE ParcelId IN %s"
    args = (status, delivery_time_seconds, parcel_ids,)
    cursor.execute(sql, args)
    db.commit()    