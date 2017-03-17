n,m=input().strip().split(' ')
n,m=[int(n),int(m)]
temp=0
res=[0]*(n)
max1=0
res1=[]
c=-1
for a0 in range(m):


    a,b,k=input().strip().split(' ')
    a,b,k=[int(a),int(b),int(k)]
    a=a-1

    if c<a and c<b:
     for i in range(a,b):
        res[i]=res[i]+k
     #print(res)
     max1=max(res)
    c=res.index(max1)

print(max(res))


