#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(arr,length):
    jump=0
    i=0
    while i in range(length):
        try:
            if arr[i+1]==0:
                try:
                    if arr[i+2]==0:
                        jump=jump+1
                        i=i+2
                    else:
                        jump=jump+1
                        i=i+1
                except:
                    jump=jump+1
                    break
                    # continue
            else:
                jump=jump+1
                i=i+2
        except:
            break
    return(jump)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    fptr.write(str(result) + '\n')

    fptr.close()
