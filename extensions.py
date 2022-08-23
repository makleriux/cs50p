# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 18:33:33 2022

@author: makle
"""

extentions = { "gif":"image/gif", "jpg":"image/jpeg", "jpeg":"image/jpeg", "png":"image/png", "pdf":"application/pdf", "txt":"text/plain", "zip":"application/zip"}

no_ext = str("application/octet-stream")

#extract extention if there is few extention, get last one and print
def get_ext(a):
    asa = a.split(".")
    asa = asa[-1].strip(" ")
    print (extentions[asa])
    
inp = str(input("File name: "))
inp = inp.lower()

#if method find fails print something
if inp.find(".") == -1:
    print(no_ext)
else:
    
    try:
        ats = get_ext(inp)
    except Exception:
        print(no_ext)
        