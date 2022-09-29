#!/usr/bin/python3

def fizz_buzz():
    n = int(input("Input number for fizzbuzz: "))

    for d in range(1, n):
        if (n % 3 and n % 5):
            print(str(d) + "FizzBuzz")
        elif (n % 3):
            print(str(d) + "Fizz")
        elif (n % 5):
            print(str(d) + "Buzz")
        else:
            print("You didn't enter a correct value" + i + "and the end")

fizz_buzz()

