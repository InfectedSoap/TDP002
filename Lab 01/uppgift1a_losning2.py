#!/usr/bin/env python3
import sys

n = int(input("Skriv ett slutnummer: "))


def sumof(n):
 sum = 0
 while n > 0:
  sum += n
  n -= 1
 return sum

print("Summan av alla nummer till och med",(n), "är" ,(sumof(n)),)
