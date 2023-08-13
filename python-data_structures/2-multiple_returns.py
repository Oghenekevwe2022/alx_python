#!/usr/bin/python3

def multiple_returns(sentence):
    multiple_returns = __import__('2-multiple_returns').multiple_returns
    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]
    length = len(sentence)
    return length, first_char



