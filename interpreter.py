# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 00:45:12 2022

@author: makle
"""
def operator(a, b, c):
    
    if b == "-":
        return int(a) - int(c)
    elif b == "+":
        return int(a) + int(c)
    elif b == "*":
        return int(a) * int(c)
    elif b == "/":
        return int(a) / int(c)


inp = str(input("Enter the arithmetic expression: "))
mylist = inp.split
op = mylist().pop(1)
x = mylist().pop(0)
y = mylist().pop(2)

print(float(operator(x, op, y)))

