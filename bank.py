# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:17:36 2022

@author: makle
"""

#get user input as greeting
#if it hello return 0
#if its starts h return 20
# if its not hello return 100

inp = str(input("Greeting: "))
inp = inp.lower()
test = "hello"

if test in inp:
    print("$0")
elif inp[0] == test[0]:
    print("$20")
else:
    print("$100")