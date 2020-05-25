# abcdefghijklmnopqrstuvwxyz
string = list(input())
k=int(input())
i=0
# print(len(string),k)
for i in range (int(len(string)/k)):
    lst=[]
    for word in string[k*i:k*i+k]:
        if word not in lst:
            lst.append(word)
    for i in lst:
        print(i,end='')
    print('\n',end='')