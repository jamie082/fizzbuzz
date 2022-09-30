#!/usr/bin/python3

import pdb

fizzbuzz = "FizzBuzz"
buzz = "Buzz"
fizz = "Fizz"

for d in range(51):
    if (d % 3 == 0 and d % 5 == 0):
         print(fizzbuzz, end=" ")
         continue
    elif (d % 3 == 0): 
         print(fizz, end=" ")
         continue
    elif (d % 5 == 0):
         print(buzz, end=" ")
         continue

         print(d)
