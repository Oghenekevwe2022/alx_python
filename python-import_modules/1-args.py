#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    inputArgs = sys.argv
    argcount = len(inputArgs) - 1
    # print (len(inputArgs) - 1, "arguments:")
    if argcount < 1:
        print(argcount, "arguments.")
    elif argcount == 1:
        print (argcount, "argument:")
    elif argcount > 1:
        print (argcount, "arguments:")
    for i, inputArgs in enumerate(inputArgs[1:], 1):
        # print(f"{i}: {arg}")
        print("{}: " "{}".format(i, inputArgs))

    

