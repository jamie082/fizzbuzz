#!/usr/bin/python3

def fizz_buzz():
    n = int(input("Input number for fizzbuzz: "))

    for d in range(1, n+1):
        if ((n % 3 and n % 5)):
            print(str(d), + d.replace(n, "FizzBuzz", end=' ')
        elif (n % 3): 
            print(str(d), + d.replace(n, "Fizz"), end=' ')
        elif (n % 5):
            print(str(d), + d.replace(n, "Buzz"), end=' ')

fizz_buzz()

