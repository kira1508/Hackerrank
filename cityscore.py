t=int(input())
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
max=0
max1=0
c=0
for i in range(len(a)):
    if max<a[i]:
        #print(a[i])
        max=a[i]
        c=c+1
for i in range(len(b)):
    if max1<b[i]:
        max1=b[i]
        c=c+1

print(c)