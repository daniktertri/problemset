n,k = map(int,input().split(' '))
z = list(map(int,input().split(' ')))
t=0
for i in range(0,n):
    if z[k-1] == 0 and z[k-1] == z[i]:
        t = t + 0
    elif z[k-1]<= z[i]:
        t = t + 1
    else:
        t = t + 0
print(t)
