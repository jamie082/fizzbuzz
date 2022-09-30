#!/usr/bin/python3

import pdb

fizzbuzz = "FizzBuzz"
buzz = "Buzz"
fizz = "Fizz"

def fizz_buzz():
    n = int(input("Input number for fizzbuzz: "))

    for d in range(1, n+1):
        if (n % 3 and n % 5):
            print(d, end=" ")
        elif (n % 3): 
            print(d, end=" ")
        elif (n % 5):
            print(d, end=" ")
        else:
            print("Error! No match found!")

fizz_buzz()
