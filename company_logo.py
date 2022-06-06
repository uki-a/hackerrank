import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d = {}
    
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
            
    d = sorted(d.items(), key=lambda x: (x[1] * -1, x[0]))
    
    
    for moji, num in d[:3]:
        print(moji, num)
