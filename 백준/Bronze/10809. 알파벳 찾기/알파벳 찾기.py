a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

b = list(input())

for i in a:
    if i in b:
        for j in b:
            if j == i:
                print(b.index(j),end=' ')
                break
    else:
        print(-1,end=' ')
        
