
def safe_print_division(a, b):
    safe_print_division = __import__('3-safe_print_division').safe_print_division
    return a/b

try:
    a = 12
    b = 2
    result = safe_print_division(a, b)
    # print("{:d} / {:d} = {}".format(a, b, result))
except:
     print("{:d} / {:d} = {}".format(a, b, result))
finally:
    print(safe_print_division(12, 2))











# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
