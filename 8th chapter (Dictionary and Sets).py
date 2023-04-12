dict = {'Name': 'Azra', 'Age': 1, 'Class': 'First'}
print ("dict ['Name']: ", dict['Name'])
print ("dict ['Age']: ", dict['Age'])

dict = {'Name': 'Azra', 'Age': 1, 'Class': 'First'}
dict['Age'] = 8; #updated age
dict['School'] = "Primary School" #new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict = {'Name': 'Azra', 'Age': 1, 'Name': 'Buket'}
print = ("dict['Name']: ", dict['Name'])

dict = {'Name': 'Azra', 'Age': 1, 'Class': 'First'}
del dict['Name'] #remove 'Name' element
dict.clear()
del dict
print ("dict['Age']: ", dict['Age'])
#Exception raised, because dictionary deleted and doesnt exist


phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
value = phonebook.get('Katie')
print(value)

for key, value in phonebook.items():
    print(key, value)
phonebook.clear()

###

myset = set([1, 2, 3, 4, 5])
print(len(myset))

myset = set()
myset.add(1)
myset.add(15)
print(myset)

myset.update([4, 5, 6])
print(myset)

myset.remove(6)
print(myset)

newset = set(['a', 'b', 'c'])
for val in newset:
    print(val)
print(newset)

set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set([7,8,9,10])
print(set1)
print(set2)

set4 = set1.union(set2) #Birlesim
print(set4)
set5 = set1.intersection(set2) #Kesisim
print(set5)
set6 = set1.difference(set2) #1. listenin 2.den farkli olan degerleri
print(set6)
set7 = set1.symmetric_difference(set2) #İki listenin ortak olmayan degerleri
print(set7)