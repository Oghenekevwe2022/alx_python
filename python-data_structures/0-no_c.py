#!/usr/bin/env python3

def no_c(my_string):
    no_c = __import__('0-no_c').no_c
    new_string = ""
    
    for char in my_string:
        if char != "c" and char !="C":
            new_string += char
    return new_string
    

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))



