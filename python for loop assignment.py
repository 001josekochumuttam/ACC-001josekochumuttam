#q1
print('QUESTION1')
for i in range(11):
    print(i)

#q2
print('QUESTION2')
for i in range(10,22,2): #the step is the last number and deciding how to iterate, 2 every 2nd digit
    print(i)

#q3
print('QESTION3')
for i in range(12,0,-2):
    print(i)

#q4
print('QUESTION4')
for i in range(0,11):
    print(i * i, i * i * i)
    
#q5/6
print('QUESTION5/6')
d = '*'
user = int(input('enter the amount of rows you wish to have'))
for num1 in range(user):
    for num2 in range(num1):
        print('*', end = '')
    print()
    
#q7
variable = 1
for num1 in range(5):
    variable2 = int(input('enter an integer'))
    variable = variable * variable2
    print(variable)

           
                
     