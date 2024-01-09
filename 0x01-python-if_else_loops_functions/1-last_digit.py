#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nax = str(number)
last_digit = int(nax[-1])
if(last_digit > 5 ):
    print("last_digit of " + nax + " is " + str(last_digit) + " and is greater than 5")
elif(last_digit == 0):
    print("last_digit of " + nax + " is " + str(last_digit) + " and is 0")
elif(last_digit < 5):
    print("last_digit of " + nax + " is " + str(last_digit) + " and is less than 6 and not 0")
