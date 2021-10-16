import math
import os
import random
import re
import sys
from collections import Counter

def counter(s):
    s = s.strip()
    data = dict(Counter(s))
    transpose = {}
    for key, value in data.items():
        if value not in transpose:
            transpose[value] = [key]
        else:
            transpose[value] += [key]
            
    tmp = sorted(transpose.items(), key=lambda r:r[0], reverse=True)
    
    t = sorted(tmp[0][1])
    formatter = "{0} {1}"
    if len(transpose.keys()) == 1:
        
        for value in t[:3]:
            if value in data:
                print(formatter.format(value, data[value])) 
    
    else:
        t += sorted(tmp[1][1])
        if len(t) >= 3:
            for value in t[:3]:
                if value in data:
                    print(formatter.format(value, data[value]))
        else:
            t += sorted(tmp[2][1])
            for value in t[:3]:
                if value in data:
                    print(formatter.format(value, data[value]))

if __name__ == '__main__':
    s = input()
    counter(s)
