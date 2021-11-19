#Q1
print('QUESTION1')
str1 = '''Pyhton
is
really
fun'''
print(str1)

#Q2
print('QUESTION2')
numAlph = input('type numbers and letters')
total = 0
for ch in numAlph: #crating for loop to convert characters into numbers
    if ch.isdigit():
        total = total + int(ch) #loop to add each number to the total which starts at 0
print(total)

#Q3
print('QUESTION3')
string = input('type words with inbetween each word')
for ch in string:
    if ch == ' ': #== means comparison
        print('-')
    else:
        print(ch)
        
#Q3 OTHER METHOD
print('other method')
sen = input('enter a sentence')
sen = sen.replace((' '), ('-'))
print(sen)

#Q4




