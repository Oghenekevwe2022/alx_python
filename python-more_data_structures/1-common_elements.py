#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_elements = __import__('1-common_elements').common_elements
    c_set = set()

    for element in set_1:
        if element in set_2:
            c_set.add(element)

    return c_set


set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
# print(sorted(list(c_set)))
# print(c_set)
