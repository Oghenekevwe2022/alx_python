#!/usr/bin/python3
def raise_exception(a, c):

    raise_exception = __import__('4-raise_exception').raise_exception
    
try:
    raise_exception("Helloworld")
except TypeError as te:
    print("Exception raised")
    