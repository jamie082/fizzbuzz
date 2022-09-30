#!/usr/bin/python3

import pdb

fizzbuzz = "FizzBuzz"
buzz = "Buzz"
fizz = "Fizz"

def fizz_buzz():
    for d in range(51):
        if (d % 3 == 0 and d % 5 == 0):
            print(fizzbuzz, end=" ")
        elif (d % 3 == 0): 
            print(fizz, end=" ")
        elif (d % 5 == 0):
            print(buzz, end=" ")

        print(d)
