#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    return(s.count('a')*(n//len(s))+s[:n%len(s)].count('a'))
    
    """For small n"""
    # i=0
    # sb=''
    # while len(sb)<=n:
    # sb=sb+s
    # sb=sb[:n]
    # wordCount={}
    # for i in range(n):
    #     wordCount[sb[i]]=wordCount.get(sb[i],0)+1
    # print(wordCount['a'])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()