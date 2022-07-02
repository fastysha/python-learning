
# def is_polyndrom(number:int) -> bool:
#     number=str(number)
#     reversed_str = str(number[::-1])
#     return str(number) == reversed_str

def is_polyndrom(number:int) -> bool:
    number=str(number)
    for index in range(0,len(number)):
        if number[0]==number[-1]:
            pass
    
print(is_polyndrom(0)) # true
print(is_polyndrom(1)) # true
print(is_polyndrom(10)) # false
print(is_polyndrom(11)) # true
print(is_polyndrom(222)) # true
print(is_polyndrom(345543)) # true
print(is_polyndrom(787)) # true
print(is_polyndrom(1002)) # false
print(is_polyndrom(533)) # false