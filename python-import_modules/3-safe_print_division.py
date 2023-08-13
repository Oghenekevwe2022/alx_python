#!/usr/bin/python3

def safe_print_division(a, b):
    safe_print_division = __import__('3-safe_print_division').safe_print_division
    return (a/b)

try:
    a = 12
    b = 2
    result = safe_print_division(a, b)
    # print("{:d} / {:d} = {}".format(a, b, result))
except:
    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("Inside result: {:d} / {:d} = {}".format(a, b, result))
finally:
#     print(safe_print_division(12, 2))
    print("Inside result: {:d} / {:d} = {}".format(a, b, result))














