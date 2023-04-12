#WHILE LOOP

while True: #Sonsuza kadar calisiyor
    print("Hello Python!") # Stop with CTRL+C


i = 1
while i < 6:
    print(i)
    i = i + 1 # it can also write i += 1


count = 0
while (count < 9):
    print("The count is: ", count)
    count = count + 1
print("Good bye!")

#Else Statement in While Loop

mycount = 0
while mycount < 5:
    print(mycount, " is less than 5")
    mycount = mycount + 1
else:
    print(mycount, " is not less than 5")
    
#FOR LOOP

i = 0
for i in range(6):
    print(i)


for x in range(2, 6):
    print(x)


for x in range(2, 30, 3):
    print(x)
    
#Else Statement in For Loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

###

num_students = int(input('How many students do you have? '))
num_test_scores = int(input('How many test scores per student? '))

for student in range(num_students):
    total = 0.0
    print('student number ', student + 1)
    print('-------------------')
    for test_num in range(num_test_scores):
        print('Test number ', test_num + 1, end='')
        score = float(input('Score:'))
        total += score
        average = total / num_test_scores
    print('The average for student number ', student + 1, 'is: ', average)
print()

#Loops for Strings

for letter in 'Python':
    print('Current Letter:',letter)
    
#Loops for Lists

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('Current fruit: ', fruit)
else:
    print('Goodbye')

#NESTED LOOPS

for i in range(1, 11):
    for j in range(1,11):
        print(i * j, end=' ')
    print()


for i in range(1, 11):
    for j in range(1,11):
        print('%d * %d = %d' % (i, j, i*j))
    print()
    

x = -20
y = 20
while x <= y:
    print('x is now: ', x)
    x = x + 1
    while x < 0:
        print('x is negative')
        x = x + 1
