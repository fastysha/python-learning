from sm_data_models import User

def map_to_user(user_dict: dict) -> User:
    return User(id=int(user_dict['UserID']), 
    name=user_dict['UserName'], 
    surname=user_dict['UserSurname'], 
    phone_number=user_dict['UserPhoneNumber'], 
    country=user_dict['Country'])