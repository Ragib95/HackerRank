#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    k = int(raw_input())
    
    #print arr
    for arr in sorted(arr, key=lambda x: x[k]):
        print ' '.join(map(str,arr))
