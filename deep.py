# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:37:46 2022

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe 
and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

@author: makle
"""

ans = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?: "))
gAns = ["42", "forty two", "forty-two"]
ans = ans.lower()
ans = ans.strip(" ")
if ans in gAns:
    print("Yes")
else:
    print("No")