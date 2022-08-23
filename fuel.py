# -*- coding: utf-8 -*-
"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 
1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an 
integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, 
output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is 
essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) 
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
def main():
    a = prom("Fraction: ")    
    a = convert(a)
    print(a)   

def prom(b):
    while True:
        try:
            a = input(b)
            if allow(a) is True:
                return a
        except Exception:
            pass

def convert(a):
    a = a.split("/")
    a = round(int(a[0]) / int(a[1]) *100)
    a = check(a)
    return a

def check(a):
    if 1 < a < 99:
        return str(a)+"%"
    elif 1 >= a:
        return "E"
    else:
        return "F"

def allow(a):
    x = ["0","1","2","3","4","99","100"]
    b = a.split("/")
    if  b[0] in x and "/" in a and b[1] != "0" and b[1] in x :
        return True
    else:
        False
    
main()

"""
In a file called fuel.py, implement a program that: 
    prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
    
    and then outputs:
        as a percentage rounded to the nearest integer, how much fuel is in the tank. 
        
        If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
        And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

"""