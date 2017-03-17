t =int(input())
w=list(map(int,input().split(' ')))
w.sort()
m=w[0]
y=w[0]+4
c=0
for i in range(t):
    if w[i]<=y:
        continue
    else:
        c=c+1
        m=w[i]
        y=m+4
print(c+1)