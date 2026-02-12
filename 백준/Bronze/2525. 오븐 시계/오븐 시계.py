a,b= map(int,input().split())
c = int(input())
sum = a*60+b+c

print(int(sum/60%24),sum%60)