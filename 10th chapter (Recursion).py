def main():
    message()

def message():
    print('This is a recursive function.')
    message()
    
main()
###

def main():
    message(5)
    
def message(times):
    if times > 0:
        print('This is a recursive function.')
        message(times - 1)
        
main()

##Factorial

def main():
    number = int(input('Enter a nonnegative integer: '))
    fact = factorial(number)
    print('The factorial of', number, 'is', fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
main()

##Fibonacci

def main():
    print('The first 10 numbers in the')
    print('Fibonacci series are:')
    for number in range (1,11):
        print(fib(number))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
    
main()
