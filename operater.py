a=int(input('enter first number: '))
b=int(input('enter any number'))
print('print 1 for +: ')
print('print 2 for -: ')
print('print 3 for *: ')
print('print 4 for /: ')
c=int(input('enter choice'))
if c==1:
     print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
    
else:
    print("wrong choice")  


