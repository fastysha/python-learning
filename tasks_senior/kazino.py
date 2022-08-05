import random

print("Hello!!It is kazino!You have 5 attempts!Enter your amount:")

amount=int(input())
money=amount
list=["A","B","C"]
a=1

def randomaizer():
        attempt=random.choices(list,k=3)
        return attempt

while a<6:
    a+=1
    res=(randomaizer())
    print(res)
    print("          ")
    if res==["A","A","A"]:
        print("X10 to your money")
        money=(money*10)
    elif res==["B","B","B"]:
        print("X2 to your money")
        money=(money*2)    
    elif res==["C","C","C"]:
        print("You lost half the money")
        money=(money/2)
    elif res==["A","B","C"]:
        a-=1
        print("You won another try")      
    else:print("Take it another time")
    print("Your balance:",money)
    print("___________________")
    next=input()
    
print("It is finish!Your balance:",money)