import os
import sys

def simpleArraySum(ar):
    series = [0]*int(ar_count)
    for i in range(len(ar)):
        series[i]= int(ar[i])
    return(sum(series))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = simpleArraySum(ar)

print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
