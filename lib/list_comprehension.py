#!/usr/bin/env python3

def return_evens(num_list):   
    n = [num for num in num_list if num % 2 == 0]
    if 0 in n:
        return n
    else: return []

def make_exclamation(sentence_list):
    if sentence_list == []:
        return []
    else: 
        n = [s + '!' for s in sentence_list ]
        return n
    pass