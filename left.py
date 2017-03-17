
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
c=abs(n-k)%n
res=[]
res[0:c]=a[-c:]
res[c:n+1]=a[0:n-c]
print(*res, sep=' ')