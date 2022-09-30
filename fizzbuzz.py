#!/usr/bin/python3

import pdb

fizzbuzz = "FizzBuzz"
buzz = "Buzz"
fizz = "Fizz"

for d in range(51):
    if (d % 3 == 0 and d % 5 == 0):
         print(fizzbuzz)
         continue
    elif (d % 3 == 0): 
         print(fizz)
         continue
    elif (d % 5 == 0):
         print(buzz)
         continue

         print(d)
