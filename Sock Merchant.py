n = int(input())
ar = list(map(int, input().rstrip().split()))

wordCount={}
k=0

lst=[0]*n
for i in range (len(lst)):
        lst[i]=ar[i]
for i in lst:
    wordCount[i]=wordCount.get(i,0)+1
    if int(wordCount[i])%2==0:
        k=k+1
print(k)