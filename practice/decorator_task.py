import random
def dec_in_dec(num:int):
    def decorator(func):
        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            return num*[res]
        return wrapper
    return decorator

@dec_in_dec(2)
def get_random_int(max):
    return random.randint(0,max)
    
@dec_in_dec(3)
def get_username():
    return 'Radislav'


print(get_random_int(20)) # -> [1]
print(get_username()) # -> ["Radislav"]