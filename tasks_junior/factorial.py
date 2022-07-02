def factorial(number:int) -> int:
    factorial=1
    for i in range(1,number+1):
        factorial*=i
    return factorial

# Factorial formula: n! = 1*2...n

print(factorial(1)) # 1 
print(factorial(2)) # 2
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120
print(factorial(6)) # 720
print(factorial(7)) # 5040