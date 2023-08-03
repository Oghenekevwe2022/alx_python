#!/usr/bin/env python3

def validate_password(password):
    if (len(password) >= 8):
    
        lowerCase = False
        upperCase = False
        num = False
        space = True

        for char in password:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowerCase = True
            if(char.isupper()):
                upperCase = True
            if(not char.isalnum()):
                space = False

        return lowerCase and upperCase and num and space
    else:
        return False
    
        