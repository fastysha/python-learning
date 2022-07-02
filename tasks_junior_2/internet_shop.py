class User:
    def __init__(self,emaill,passward):
        self.emaill=emaill
        self.passward=passward

    def __eq__(self, other):
        return self.emaill == other.emaill

    def __hash__(self):
        return hash(self.emaill)
        
users=set()
while(True):
    print("Hello,it is my internet shop!!")
    print("1-Registration")
    print("2-Enter")
    choice_user=int(input())
    if choice_user==1:
        user_name=input("Your name: ")
        user_age=int(input("Your age: "))
        user_emaill=(input("Email: "))
        user_passward=input("Passward: ")
        
        user=User(user_emaill,user_passward)
        users.add(user)
    else:
        login=input("Your login(emaill): ")
        passward=input("Your passward: ")
        user=User(login,passward)

        print(users)
        print(User(login, passward) in users)
        
        if user in users:
            print("You enter to system ")
            break
        else:
            print("Wrong data")
        
    