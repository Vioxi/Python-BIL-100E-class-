import sys
a_list = list()
a_tuple = tuple()

a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)

print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

#Lists
print(list(' cat '))
lst1 = ['physics', 'chemistry', 2017, 2023]

print("Value available at index 2 : ", lst1[2])

#Tuples
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

tup1 = ('physics', 'chemistry', 2017, 2023)
tup2 = (1,2,3,4,5,6,7)

print("tup1[3]: ", tup1[3])
print("tup2[2:6]: ", tup2[2:6])

#Deletion
mylist = ['python', 'java', 2017, 2023]
print(mylist)
del mylist[1]
print("After deleting value at index 1: ", mylist[1])

#Update
lst2 = ['python', 'geometry', 2017, 2023]
print("Value available at index 3: ", lst2[3])
lst2[3] = 5000
print("New value available at index 3: ", lst2[3])
print("New list", lst2)

#Split
txt = 'but soft what light in yonder window breaks'
words = txt.split()
print(words)

#Two expressions
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

pow2 = []
for x in range(10):
    pow2.append(print(2 ** x))
    
#Append(Sonuna ekleme), Insert(belirli bir konuma ekleme), Extend(birden çok ekleme)
langs = []
langs.append("Python")
langs.append("Per1")
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)

langs.extend(("JavaScript", "ActionScript"))
print(langs)

#Removing
langs = ["Python", "Ruby", "Per1", "Lua", "JavaScript"]
print(langs)

del langs[1]
print (langs)

del langs[:]
print(langs)

##

s1 = "welcome "
s2 = "to "
s3 = "python "
s4 = s1+s2+s3

print(s4)

#Accessing
L = ['a', 'b', 'c']

for index, item in enumerate(L):
    print(index, item)
    
#Concatenation
hello = "hello"
python = "python"

print(hello + " " + python)
print("%s %s" % (hello, python))
print("{} {}".format(hello, python))
print(' '.join([hello,python]))

#Slicing
ss = "Shark attacks fisherman!"

print(ss[:5])
print(ss[7:])
print(ss[-4:-1])
print(ss[0:12:2])

#isalpha() [Only alphabetic]
mystr1 = "this"
print(mystr1.isalpha())

mystr2 = "this is tring example...wow!!!"
print(mystr2.isalpha())

#islower() [All lowercase]
mystr3 = "THIS is string example...wow!!!"
print(mystr3.islower())

mystr4 = "this is string example...wow!!!"
print(mystr4.islower())

#isspace() [Only whitespace]
mystr5 = "       "
print(mystr5.isspace())

mystr6 = "this is not a space"
print(mystr6.isspace())

#strip() [Remove all beginning and end of the characters]
mystr7 = "0000000000this is string example.wow!!!000000"
print(mystr7.strip( '0' ))

#lstrip
mystr8 = "        this is string example.wow!!!!"
mystr9 = "8888888this is string example...wow!!!8888888888"

print(mystr8.lstrip())
print(mystr9.rstrip('8'))

#endswith() [Check is it ending substring]
mystr12 = "this is string example...wow!!!"

suffix = "wow!!!"
print(mystr12.endswith(suffix))
print(mystr12.endswith(suffix,20))

suffix = "is"
print(mystr12.endswith(suffix, 2, 4))
print(mystr12.endswith(suffix, 2, 6))

#startswith()
mystr13 = "this is string example...wow!!!"

print(mystr13.startswith( 'this' ))
print(mystr13.startswith( 'is', 2, 4 ))
print(mystr13.startswith( 'this', 2, 4 ))
