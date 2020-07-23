#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countA=0
    countB=0
    for i in apples:
        if a+i in range(s,t+1):
            countA=countA+1
    for i in oranges:
        if b+i in range(s,t+1):
            countB=countB+1
    print(countA)
    print(countB)

st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
