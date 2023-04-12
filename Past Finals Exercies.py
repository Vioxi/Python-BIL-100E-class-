f = open("test31.txt", "w+")
f.write("x")

data = x
i = f.readline()
while i != x:
    data += i
    i = f.readline()
    
data = f.read()

data = 
for i in f:
    data += i
    
data = f.input()

##

class Sales:
    def __init__(self, id):
        self.id = id
        id = 100
        
val = Sales(123)
print(val.id)

##
f = open("names.txt", "w+")
f.write("asdfasdfasdf\nasdfasdfasdfasdf")

f = open('names.txt', 'r')

for line in f:
    print(line)
f.close()


##
class Student:
    def __init__(self):
        self.name = "John"
        self.surname = "Smith"
    def __str__(self):
        return "My name is " + self.name + " " + self.surname
    

print(Student().__str__())

Student().__str__()
