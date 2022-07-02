import random
import datetime
print("Хей,это игра,введи диапазон чисел")
min = int((input("От: ")))
max = int((input("До: ")))

random_number = random.randint(min, max)
counter=1
print("Я загадал,теперь угадывай")
answer = random_number + 1
start_time=datetime.datetime.now()
while(answer != random_number):
    answer = int(input("Твоё число: "))
    if answer>max or answer<min:
        print("Выход за диапазон")
    elif (answer > random_number):
        print("Меньше")
        counter+=1 
    elif (answer<random_number):
        print("Больше")
        counter+=1
else:
    finish_time=datetime.datetime.now()
    end=finish_time-start_time
    print("УГАДАЛ! Попыток: " + str(counter))
    print("Потрачено времени:",end.seconds)
 