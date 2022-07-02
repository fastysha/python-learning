import random

dictionary={
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "10":0
}
for x in range(0,100):
    number=random.randint(1,10)
    key=str(number)
    dictionary[key]=dictionary[key]+1
for key,value in dictionary.items():
    print(key,value)