#!/usr/bin/python3
# def raise_exception(a, c):
#     raise_exception = __import__('4-raise_exception').raise_exception
    
# try:
#     raise_exception()
# except TypeError as te:
#     print("Exception has been raised")

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


    