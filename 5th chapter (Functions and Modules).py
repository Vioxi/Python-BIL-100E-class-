##FUNCTIONS

# 1-Value returning functions

def myprint(s1):
    print(s1)
myprint("Barcelona")

#Return Statement

def my_function(x):
    return 5 * x
print(my_function(3))

def Fun(x,y):
    result=x+y
    return result
print(Fun(3,5))

# 2-Pass by reference

def ChangeRefer(mylist):
    mylist = [1,2,3,4]
    print("First values ", mylist)
    
mylist = [10,20,30]
ChangeRefer(mylist)
print("Secondary values: ", mylist)

def printinfo(name, age=23):
    print("Name: ", name)
    print("Age: ", age)
printinfo(age = 19, name = "Tasmanian Devil")    
printinfo(name= "Bugs Bunny")


# 3-Random Number Generation

from random import randint
print(randint(0,100))

import random #It is same thing with upper code
print(random.randint(0,100))

##RANDRANGE FUNCITON / RANDOM MODULE

import random

print ("Random number from 0-100 is : ", end="")
print (random.randrange(100))

print ("Random number from 50-100 is : ", end="")
print (random.randrange(50,100))

print ("Random number from 50-100 skip is : ", end="")
print (random.randrange(50,100,5))


import random
print("randrange(100, 1000, 2) : ", random.randrange(100,1000,2))

import random
print("randrange(100, 1000, 3) : ", random.randrange(100,1000,3))

#UNIFORM FUNCTION / RANDOM MOFULE

print("Random float uniform(18,81): ", random.uniform(18,81))
print("Random float uniform(19,38): ", random.uniform(19,38))

#SYS MODULE / SYS.PATH

import sys
print(sys.path)

import math
print(math.pi)

from math import pi
print(pi)

import math
def area_of_a_circle(r):
    a = r**2 * math.pi
    return a
print(area_of_a_circle(3))
