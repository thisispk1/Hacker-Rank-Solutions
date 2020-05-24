# Absolute difference of Diagonals
arr = [[11,2,4],[4,5,6],[10,8,-12]]
n = len(arr)
sum1=sum2=0
for i in range (n):
    sum1 = sum1 + arr[i][i]
    # print(arr[i][i])
    # print(sum1)
    sum2 = sum2 + arr[i][-i-1]
    # print(arr[i][-i-1])
    # print(sum2)
print(abs(sum1-sum2))