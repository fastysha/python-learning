# def reverse(s:str) -> str:
#     reverse_str=str(s[::-1])
#     return reverse_str

def reverse(s:str) -> str:
    rs = ''

    # 0 1 2
    # d o g 

    # g = len(s) - 1 - index = 2
    # o = len(s) - 1 - index = 1
    # d - len(s) - 1 - index = 0 

    # -1  -2  -3
    # g  o  d
    for index in range(0, len(s)):
        rs+=s[0 - 1 - index] # g d o
    return rs

# The method reverses the text value

print(reverse('')) # 
print(reverse('s')) # s
print(reverse('dog')) # god
print(reverse('reverse')) # esrever
print(reverse('1234')) # 4321
print(reverse('001hello001')) # 100olleh100