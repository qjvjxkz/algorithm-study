a = int(input())

lst = [[0]*100 for i in range(100)]

for i in range(a):
    c,b = map(int,input().split())
    for j in range(c,c+10,1):
        for k in range(b,b+10,1):
            lst[j][k] = 1

sum = 0
for row in lst:
    for val in row:
        sum+=val

print(sum)