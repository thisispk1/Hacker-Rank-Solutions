str=bin(int(input()))[2:]
print(str)
max=0
count=0
for i in range(len(str)):
    if int(str[i]) == 1:
        count=count+1
        try:
            if int(str[i+1])==1 :
                continue
        except:
            if max<count:
                max=count
            break
    else:
        if max<count:
            max=count
        count=0
print(max)