t = int(input())
i = 0
for j in range(t):
    p,v,t = map(int,input().split(' '))
    if (p+v+t) >=2:
        i+=1
print(i)
