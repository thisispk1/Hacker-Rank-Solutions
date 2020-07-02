#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    # print(a)
    maxlen=None
    for m in a:
        lt=[]
        for n in range(a.index(m),len(a)):
            if abs(m-a[n])<=1:
                lt.append(a[n])
            if maxlen==None or maxlen<len(lt):
                maxlen=len(lt)
    return(maxlen)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
