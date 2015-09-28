#!/usr/bin/env python3
import sys

n = int(input("Skriv ett slutnummer: "))


def factorial(n):
 product = 1
 while n > 0:
  product *= n
  n -= 1
 return product

print("Produkten av alla nummer till och med",(n), "är" ,(factorial(n)),)
