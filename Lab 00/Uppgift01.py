#!/usr/bin/env python3
#-*- coding: utf-8 -*-
def temp():
    if __name__ == '__main__':
        print("Running as a program")
    else:
        print("Running as a module")

def num_stuff(x):
    """Adds 5 to the supplied number"""
    return x + 5

if __name__ == '__main__':
    temp()
def print_name():
    print(__name__)
