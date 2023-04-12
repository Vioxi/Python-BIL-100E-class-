#EBOB Bulucu (Recursive)

def gcd(a,b):
    a, b = b % a, a
    if a == 0:
        return b
    else:
        return gcd(a, b)

print(gcd(4, 8))
print(gcd(42, 28))
print(gcd(28, 42))
print(gcd(345, 766))

#İngilizce-Türkçe Sözlük (Dictionary)

book = {}
s = int(input("How many English world did you learn?"))

for i in range(s):
    eng=input('Enter an English word:')
    tur=input('Enter its meaning in Turkish:')
    book[eng] = tur

print('English', 'Turkish', sep='   ')
print('-----------------')

for key, value in sorted(book.items()):
    print(key,value,sep='   ')
    print()
    
#Kelimeyi Ters Çevirici (Recursive)

def main():
    s=input("Place enter word:")
    reverseStr(s)
    print("Senin kelimen:", reverseStr(s))
    
def reverseStr(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverseStr(s[1:]) + s[0]

main()

#Bingo Oyunu

from random import randrange
NUMS_PER_LETTER = 15

def createCard():
    card = {}
    lower = 1
    upper = 1 + NUMS_PER_LETTER
    for letter in ["B", "I", "N", "G", "O"]:
        card[letter] = []
        while len(card[letter]) != 5:
            next_num = randrange(lower, upper) 
            #İlk iterasyon 1 ile 15 arasında sayı üretiyoruz
            if next_num not in card[letter]:
                card[letter].append(next_num)    
        lower = lower + NUMS_PER_LETTER
        upper = upper + NUMS_PER_LETTER # 5x5 matris 
        #2. sıra için 14+1=15 New Lower / 15+15=30 New upper band
    return card

def displayCard(card):
    print("B I N G O")
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d " % card[letter][i], end="")
        print()
    
def main():
    card = createCard()
    displayCard(card)

if __name__ == "__main__":
    main()
    
#Random Number Generator

import random

def main():
    number_dict = dict()
    for i in range(10000):
        random_number = random.randint(1,10)
        if random_number not in number_dict:
            number_dict[random_number] = 1 
            #Eğer sözlüğünde bu değer hiç yoksa ilk indeks değerini ata 
        else:
            number_dict[random_number] += 1 
            #Eğer aynı sayı varsa indeksini 1 arttır
    
    print('Number\tFrequency')
    print('------  ---------')
    
    for number, frequency in sorted(number_dict.items()):
        print(number, frequency, sep='\t')

main()

#Soğuk Sıcak Oyunu (Numara Tahmin)

import random

def main():
    number = random.randint(1, 100)
    correct_number, count=playGuessingGame(number)
    
    print('Thanks for playing!', correct_number, 'is your lucky number. \
But you have tried', count, 'Times!')

def playGuessingGame(number):
    count = 0
    userGuess = int(input('Enter a number between 1 and 100: '))
    
    while userGuess > 0:
        if userGuess > number:
            print('Too high, try again')
            userGuess = int(input('Enter a number between 1 and 100: '))
            count += 1
        elif userGuess < number:
            print('Too low, try again')
            userGuess = int(input('Enter a number between 1 and 100: '))
            count += 1
        else:
            print('Congratulations! You guessed the right number!')
            count += 1
            return userGuess,count

main()

#Çarpma Makinesi (Recursive)

def main():
    num1 = 0
    num2 = 0
    
    while num1 <= 0:
        num1 = int(input('Enter the first number: '))
        
    while num2 <= 0:
        num2 = int(input('Enter the second number: '))
        
    print(num1, 'times', num2, 'is', multiply(num1, num2))

def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1) #x ve y 0 olana kadar x leri yan yana topluyor
    
main()


