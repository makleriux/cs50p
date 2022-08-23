# -*- coding: utf-8 -*-
"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""

"""

In a file called grocery.py, implement a program that: 
    ----prompts the user for items, 
    ----one per line, 
    ----until the user inputs control-d (which is a common way of ending one’s input to a program). 
    
    -----Then output the user’s grocery list in all uppercase, 
    -----sorted alphabetically by item, 
    prefixing each line with the number of times the user inputted that item. 
    
    No need to pluralize the items. 
    Treat the user’s input case-insensitively.

"""

def main():
    prom("Item: ")

def h_lifting(lista):
    new_list = []
    lista.sort()
    a_up = [i.upper() for i in lista]
# predefine dictionary
    dic = {}
    x = 1
    a = 0
# counting items 
    for i in a_up:
        if i in dic:
            x = x+1
            dic[i] = x
        else:
            x=1
            dic[i] = x
            new_list.append(i)
# printing out
    for x in dic:
        print(dic[x], new_list[a])   
        a = a +1
    
def prom(a):
    shop_list = []
    while True:    
        try:
            item = input(a)
            shop_list.append(item)                     
        except EOFError:   # Catch the Ctrl-D
            shop_list = h_lifting(shop_list)        
            return shop_list
        except Exception:   # Trap all other errors
            pass
        
main()