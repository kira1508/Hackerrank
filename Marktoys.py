n,k=input().split(' ')
n,k=[int(n),int(k)]
sum=0
c=0
res=list(map(int,input().split(' ')))
res.sort()
for i in range(n):
    sum=sum+res[i]
    if sum<=k:
     #print(res[i])
     c=c+1
    else:
        sum=abs(res[i]-sum)
        continue

print(c)