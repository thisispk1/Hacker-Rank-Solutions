# Input string
a = [1,2,3]
b =[2,3,3]

# Comparison
score= [0,0]
# scrcom1 = [a[0]>b[0], a[1]>b[1], a[2]>b[2]]
# # scrcom2 = [a[0]<b[0], a[1]<b[1], a[2]<b[2]]
# scrcom3 = [a[0]==b[0], a[1]==b[1], a[2]==b[2]]
# # for n in scrcom1 :
#     # print('in')
#     if n == True:
#         score[0] = score[0]+1
#         # print('a=',score[0])
#     else:
#         score[1] = score[1]+1
#         # print('b=',score[1])
#     for n in scrcom3 :
#         if n == True:
#             score[0] = score[0]+1
#             score[1] = score[1]+1

for i in range(3):
    if a[i] > b[i]:
        score[0] = score[0]+1
    if a[i] < b[i]:
        score[1] = score[1]+1
    else:continue
print(score)