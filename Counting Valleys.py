def countingValleys(n, s):
    # valley=0
    # arr=[]
    # letCount={'D':0,'U':0}
    # for letter in s:
    #     if letter == 'U':
    #         arr.append(1)
    #     if letter == 'D':
    #         arr.append(-1)
    # for i in range(0,n):
    #     if sum(arr[:i])==0 and arr[i]==-1:
    #         # print(i,sum(arr[:i]),arr[i])
    #         valley=valley+1
    # print(valley)

    # or
    
    altitude=valley=0
    for i in range(n):
        if(s[i]=='U'):
            altitude+=1
            if(altitude==0):
                valley+=1
        else:
            altitude-=1    
    print(valley)

n = int(input())
s = input()
countingValleys(n, s)