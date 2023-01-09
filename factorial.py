

def fact(a):
    if a==1:
        return 1
    else:
     return fact(a-1)*a 

Num = int(input('enter the number: '))
print (fact(Num))

