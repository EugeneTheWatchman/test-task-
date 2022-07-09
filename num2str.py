# -*- coding: utf-8 -*-

d = {'1': 'one','2': 'two','3': 'three','4': 'four','5': 'five','6': 'six','7': 'seven','8': 'eight','9': 'nine','0': 'zero'}
def num_to_text(num):

    if num in d.keys():
        return d[num]
    return num