count = int(input())
a=list(map(int,input().split()))

m = max(a)

a= [x/m*100 for x in a]

print(sum(a)/len(a))