#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    update_dictionary = __import__('2-update_dictionary').update_dictionary
    a_dictionary[key] = value
    
    def print_sorted_dictionary(my_dict):
    # Print sorted dictionary

        keys = sorted(my_dict.keys())
        for k in keys:
            print("{}: {}".format(k, my_dict[k]))

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
# print_sorted_dictionary(new_dict)
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
   

