#!/usr/bin/python3
def fizzbuzz():
    for n in range(101):
        if n == 100:
            print('Buzz')
        elif n % 3 == 0 and n % 5 != 0:
            print('Fizz ')
        elif n % 5 == 0 and n % 3 != 0:
            print('Buzz ')
        elif n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz ')

