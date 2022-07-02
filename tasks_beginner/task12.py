from multiprocessing.sharedctypes import Value


numbers=(1,2,3,4,5,6,6,6,6,6,4,4,4,4,4,2,4,5,6)
dictionary={}

for x in numbers:
    key=str(x)
    if key in dictionary:
        dictionary[key]+=1
    else:
        dictionary[key]=1
print(dictionary)    
    
