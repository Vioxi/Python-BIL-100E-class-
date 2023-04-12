#BOOLEANS

print(7 > 6)
print(7 == 6)
print(7 < 6)

a = 6
b = 7

#BOOLEAN OPERATORS

#Not
#And
#Or

print(1, not a == 7 and b == 7) 
print(2, a ==7 or b == 7)
print(3, a ==7 or b == 6)
print(4, not(a == 7 or b == 6))
print(5, not a == 7 or b == 6)

#COMPARISON OPERATORS (==, !=, <, >, <==, >==)

#Equality and inequality operators ( == and != )
#Order operatores (<, >, <=, >=)

print (7 != 6)
print (not (7 == 6))
print(7 != (7 + 0.0))
print(7 == 7)

print('a > b is', a > b)
print('a < b is', a < b)
print('a == b is', a == b)
print('a != b is', a != b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)

#STRING COMPARISON

x = 'abc'
y = 'abd'
print('y > x is ', y > x)

##

string1 = "abc def ghi"
string2 = "def ghi abc"

print(string1 == string2)
print(string1 != string2)
print(string1 < string2)

##

s1 = "Mary"
s2 = "Mark"

print(s1 < s2)
print(s1 > s2)

#IF-ELSE-ELIF STATEMENTS

#IF decides whic values are truthy or falsy
#ELIF 
#ELSE

number = 10

if number == 1:
    print('one')
elif number == 2:
    print('two')
elif number == 3:
    print('Three')
else:
    print('Unknown')

#input() function

name = input('Enter your name: ')
print('Hello, ' + name)

name = input('What is your name? ')
password = input('What is the password? ')

if name == "BIL100E" and password == "Python":
    print("Welcome BIL100E Python")
elif name == "Programming" and password == "Languages":
    print("Welcome Programming Languages")
else:
    print("Cannot recognize who you are")

##

x = 0.6
y = 0.3
print(0.0 <= x <= 0.5)
print(0.5 >= y >= 0.1)

##

num = 100

if num <= 90:
    print("1- True expression value")
    print(num)
elif num == 100:
    print("2- True expression value")
    print(num)
else:
    print("3- False expression value")
    print(num)
print("Goodbbye")