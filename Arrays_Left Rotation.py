#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    rs=[None]*len(a)
    t=0
    while t<d:

        # for i in range(len(a)):
        #     rs[i-1]=a[i]
        # a=rs.copy()
        
        x=a[0]
        a.remove(x)
        a.append(x)
        
        t=t+1
    return(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
