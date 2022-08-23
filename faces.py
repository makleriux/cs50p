# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 00:40:46 2022

@author: simas simanavicius
"""
word = str(input("Please enter your text: "))

def convert (a):
        a = a.replace(":)", "🙂")
        a = a.replace(":(", "🙁")
        print(a)
        
convert(word)