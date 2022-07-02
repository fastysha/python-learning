def sum_numbers (a,b):
    return(a+b)
print(sum_numbers(1,2))

sum_lambda= lambda a,b:a+b
print(sum_lambda(1,2))

def foo(n):
    return lambda a :  lambda x:x*a*n
print(foo(2)(3)(4))

def foo1(condition,l1,l2):
    if condition:
        l1()
    else:
        l2()
foo1(2==2,lambda:print("good"),lambda:print("bad"))
foo1(2==3,lambda:print("corect"),lambda:print("wrong"))
