a=int(input("Ваш возраст:"))
if(a<18 and a>0):
    print("Малолетка")
elif(a>=18 and a<21):
    print("только пиво")
elif(a>=21 and a<70):
    print("Бухаем всё") 
elif(a>=70):
    print("Опасно для жизни")
else:
    print("невозможно")          