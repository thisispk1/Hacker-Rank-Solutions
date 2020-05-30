T=int(input())
arr=[]
for i in range(T):
    arr.append(input())
    # print(arr)
i=0

while i<T:
    even=''
    odd=''
    for n in range(len(arr[i])):
        if n%2==0:
            even=even+arr[i][n]
        else:
            odd=odd+arr[i][n]
    print(even,odd)
    i=i+1