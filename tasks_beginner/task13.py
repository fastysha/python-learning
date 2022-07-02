n=1
def foo ():
    n=2
foo()
print(n) #1


n=1
def foo2 ():
    global n
    n=2
foo2()
print(n) #2

n=1
def foo3 (n):
    n=2
foo3(n)
print(n) #2

n=1
def foo4 (n):
    n=2
    return n
n=foo4(n)
print(n) #2

