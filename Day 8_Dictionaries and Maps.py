import sys

n = int(input())
contacts={}
for i in range(n):
    l=input().split()
    contacts[l[0]]=l[1]
while True:
    name=input()
    if name in contacts:
        print(name+'='+contacts[name])
    else:
        print('Not found')