#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=0
    max=None
    for i in range(4):
        for n in range(4):
            sum = sum+int(arr[i][n]+arr[i][n+1]+arr[i][n+2]+arr[i+1][n+1]+arr[i+2][n]+arr[i+2][n+1]+arr[i+2][n+2])
            if max==None:
                max=sum
            elif max<sum:
                max=sum
            sum=0
    return(max)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
