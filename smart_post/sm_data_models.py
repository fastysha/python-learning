import enum
class ParcelStatus(enum.Enum):
    IN_PROGRESS = 1,
    DELIVERED = 2,
    RECIEVED = 3

class User:
    def __init__(self, id:int, name:str, surname:str, phone_number:str, country:str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.country = country

    def full_name(self):
        return f"{self.name} {self.surname}"
class Parcel:
    pass