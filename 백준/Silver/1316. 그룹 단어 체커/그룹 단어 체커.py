a = int(input())
ans = 0

for i in range(a):
    isVisited =[False]*26
    oK = True
    word = input()
    before = word[0]
    isVisited[ord(before)-97]=True
    
    for c in word[1:]:
        if isVisited[ord(c)-97]==True:
            if before != c:
                oK = False
                break
        else: 
            isVisited[ord(c)-97] = True
            before = c
    if oK == True:
        ans+=1

print(ans)

