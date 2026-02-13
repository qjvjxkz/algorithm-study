a,b = map(int,input().split())

lst = []
lst1 = []
for i in range(a):
    row = list(map(int,input().split()))
    lst.append(row)
for i in range(a):
    row = list(map(int,input().split()))
    lst1.append(row)

for i in range(a):
    for j in range(b):
        print(lst[i][j]+lst1[i][j],end=' ')
    print()