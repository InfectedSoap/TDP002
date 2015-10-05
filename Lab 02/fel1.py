#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factor(multiplicator):
    return 10*multiplicator

def fraction(divisor):
    return 10.0 / divisor

def power(exponent):
    return 10**exponent
 
print("with x = 1 to 10:") #Paranthesis
# print 10 multiplicated by numbers 1 to 10
numbers = []
for x in range(10):
    numbers.append(str(factor(x))) #misspelt
print("   10 multiplicated with x:", ", ".join(numbers))

# print 10 divided by the numbers 1 to 10
numbers = []
for x in range(1,10): #can't start with 0
    numbers.append(str(fraction(x)))
print("   10 divided by x:", ", ".join(numbers))

# print 10 raised to the power of the numbers 1 to 10
numbers = []
for x in range(10):
    numbers.append(str(power(x))) #add string.
print("   10 raised to x:", ", ".join(numbers))
