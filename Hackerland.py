n,k=input().split(" ")
n,k=[int(n),int(k)]
trans=list(map(int,input().split(' ')))
j=k
i=j
m=k+1
a=[]
res=[arr for arr in range(max(trans)+1)]
del res[0]
trans.sort()
while(i<len(trans)):
    a.append(trans[i])
    i=i+m
#print(a)
for i in range(len(res)):
    if res[i] in a:
        res[i]=-1
        l=i

b=res[-1]
l=l+1
if b in trans:
    if (len(res)-l)>k:
        res[-1]=-1
#print(res)
print(res.count(-1))