N=int(input())
addition = 0
debt = 0
for i in range(N+1):
    addition += int(input().split("$")[1].split(".")[1])
    if i != 0 and addition % 100 != 0:
        debt+=1
print(debt) 