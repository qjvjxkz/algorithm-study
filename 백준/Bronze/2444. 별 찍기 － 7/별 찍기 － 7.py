a = int(input())

for i in range(1,a):
    print(" "*(a-i),end="")
    print("*"*(i*2-1))

for i in range(a):
    print(" "*i,end="")
    print("*"*(a*2-(i*2+1)))