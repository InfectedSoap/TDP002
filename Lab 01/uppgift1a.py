#!/usr/bin/env python3
import sys

print("Detta script skriver ut summan av alla nummer") 
print("mellan ditt valda start- och slutnummer. \n")

start = int(input("Skriv ett startnummer: "))
end = int(input("Skriv ett slutnummer: "))

print(sum(range(start, end+1)))

