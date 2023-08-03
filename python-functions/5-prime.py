#!/usr/bin/env python3

def is_prime(number):
 if number <= 1:
   return False
 for d in range (2, number):
   if number % d == 0:
     return False
   elif number % 3 == 0:
    return False
   return True
     
        
    