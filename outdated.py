# -*- coding: utf-8 -*-
"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, 
which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. 
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. 
Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, 
no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or 
September 8, 1636, wherein the month in the latter might be any of the values in the list below:
"""
test = "September 18, 1636"

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
"""
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

def main():
    string = test
    string = find_month(test)
    string = find_seperators(string)
    string = fix_seq(string)
    print("{}-{:02}-{:02}".format(string[0], int(string[1]), int(string[2]))) 

#do we have month in the string?
#if we do change it to the digid
def find_month(string):
    b = 0
    for n in month:
        te = string.find(n)
        if te is not -1:
            testt = string.replace(n, str(b+1)+",")
            return testt
            break
        else:
            b=b+1

def find_seperators(string):
    if "," in string:
        string = string.replace(",", "")
    if "/" in string:
        string = string.replace("/", "")
    return string
    
def fix_seq(string):
    str_list = string.split(" ")
    str_list.reverse()
    return str_list

main()