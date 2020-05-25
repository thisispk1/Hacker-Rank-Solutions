# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
let=[]
i=0
while i < n:
    let.append(input())
    i=i+1
# print(let)
wordCount={}
for word in let:
    wordCount[word]=wordCount.get(word,0)+1
print(len(wordCount))
for word in wordCount:
    print(wordCount[word], end = ' ')