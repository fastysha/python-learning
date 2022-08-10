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
    cursor.execute(
        "SELECT * FROM Users WHERE UserPhoneNumber = %s", (phone_number,))
    user = cursor.fetchone()
    # print(f'Finded user by phone {phone_number} is: {user}')
    return user


def create_user(user):
    cursor = db.cursor()
    sql = "INSERT INTO Users (UserName, UserSurname,UserPhoneNumber,Country) VALUES (%s,%s,%s,%s)"
    args = (user["name"], user["surname"], user["phone_num"], user["country"])
    cursor.execute(sql, args)
    db.commit()
    print(cursor.rowcount, "record inserted.")


############################################
############# Parcels Table SQL ############
# ##########################################
def create_parcel(new_parcel):
    cursor = db.cursor()
    sql = "INSERT INTO parcels(SenderID,ConsumerID,ParcelName,Price,DestinationPostNumber,Status) VALUES (%s,%s,%s,%s,%s,%s)"
    args = (new_parcel["sender_id"], new_parcel["consumer_id"], new_parcel["name"],
            new_parcel["price"], new_parcel["post_num"], new_parcel["status"])
    cursor.execute(sql, args)
    db.commit()
    print(cursor.rowcount, "record inserted.")


def find_all_not_delivered_parcels(delivery_time_seconds: int) -> list:
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM Parcels WHERE Status = %s AND CreationDate <= (CURRENT_TIMESTAMP() - INTERVAL %s SECOND)"
    cursor.execute(
        sql, (ParcelStatus.IN_PROGRESS.name, delivery_time_seconds,))
    parcels = cursor.fetchall()
    return parcels


def update_parcels(status: str, parcel_ids: list):
    cursor = db.cursor()
    sql = "UPDATE Parcels SET Status = %s, DeliveryDate = CURRENT_TIMESTAMP() WHERE ParcelId IN (%s)"
    args = (status, ",".join(parcel_ids),)
    cursor.execute(sql, args)
    db.commit()
