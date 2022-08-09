import time

FLOORS=[1,2,3,4,5,6,7,8,9,10,11,12]
print(FLOORS)


def get_floors(floors,floor):
        new_floors=[]
        for el in floors:
            if floor==el:
                new_floors.append(f"[{el}]")
            else: 
                new_floors.append(str(el))
        return " ".join(new_floors)

def run_lift(floors,initial:int,target:int):
    if initial==target:
        print("Уже тут")
        return
    
    desired_range=None
    if initial<target:
        desired_range=range(initial,target+1)
    else:
        desired_range=reversed(range(target,initial+1))
    for curr in desired_range:
        res=get_floors(floors,curr)
        time.sleep(1)
        print(res,end="\r")
    print()

lift_position=1

while True:
    user_floor=int(input("Write your  floor: "))
    if user_floor<=0 or user_floor>len(FLOORS):
        print("нет таких этажей")
        continue
    
    # finish=int(input("Write where to go: "))
    run_lift(FLOORS,lift_position,user_floor)
    lift_position=user_floor

   



    
        




    

    


