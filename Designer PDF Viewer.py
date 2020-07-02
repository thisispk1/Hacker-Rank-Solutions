#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxheight = None
    alphabets = list(string.ascii_lowercase)
    for i in word:
        height=int(h[alphabets.index(i)])
        if maxheight==None or maxheight<height:
            maxheight=height
    return(maxheight*len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
