#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    result=''
    s=list(s.replace(" ", ""))
    r=math.ceil(len(s)**0.5)
    c=math.floor(len(s)**0.5)
    for i in range(r):
        try:
            if (len(s)**0.5)%1==0:
                for j in range(0,len(s)+1,c):
                    result+=(s[j+i])
                # print(' ',end='')
            else:
                for j in range(0,len(s)+1,c+1):
                    result+=(s[j+i])
        except:
            pass
        result+=(' ')
    return result    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
