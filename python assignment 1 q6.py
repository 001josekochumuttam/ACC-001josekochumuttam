units = int(input('enter units'))

if (units <= 100):
    print('no charge')
    
elif(100 < units <= 200):
    charge5Cents = units * 5
    print('your bill is', charge5Cents)

elif(200 < units):
    charge10Cents = units * 10
    print('your bill is', charge10Cents)


