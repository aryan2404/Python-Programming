amount = int(input('shopping amount'))
if amount<=5000:
    discount=(5*amount)/100
    print('discount: ',(5*amount)/100)
    print('pay: ',amount-discount)
elif amount>=5000 and amount<=10000:
    discount=(10*amount)/100
    print('discount: ',(10*amount)/100)
    print('pay: ',amount-discount)
elif amount>=10000 and amount<=15000:
    discount=(15*amount)/100
    print('discount: ',(15*amount)/100)
    print('pay: ',amount-discount)
elif   amount>=15000 and amount<=20000:
    discount=(20*amount)/100
    print('discount: ',(20*amount)/100)
    print('pay: ',amount-discount) 
elif amount>20000:
    discount=(0*amount)/100
    print('discount: ',(0*amount)/100)
    print('pay: ',amount-discount) 
else:
    print('wrong operation')

      

   


