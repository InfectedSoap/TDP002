#!/usr/bin/env python3
import functools
s = int(input("Skriv ett startnummer: "))
e = int(input("Skriv ett slutnummer: "))
def lcm(*values):
    values = [value for value in values]
    if values:
        n  = max(values)
        m = n
        values.remove(n)
        while any( n % value for value in values ):
            n +=m
        return n
    return 0

print(functools.reduce(lcm, range(s, e)))
