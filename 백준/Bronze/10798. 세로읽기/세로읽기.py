lst = []
for i in range(5):
    lst1 = list(input())
    lst.append(lst1)

for i in range(15):
    for j in range(5):
        try:
            print(lst[j][i],end='')
        except IndexError:
            continue