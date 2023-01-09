from operator import truediv
from pickle import TRUE


def add(a,b):
    return a+b


def substract(a,b):
    return a-b


def  multiply(a,b):
    return a*b

def divide(a ,b): 
    return a/b
    print('select opeation')
print('1.add')
print('2.substract')
print('3.multiply')
print('4.divide')

while TRUE :
    choice =('enter the choice(1/2/3/4):')
if choice in ('1','2','3','4',):
    num1 = float(input('enter the first number'))
    num2 = float(input('enter the second number'))
if choice == '1' :
    print(num1, '+')

