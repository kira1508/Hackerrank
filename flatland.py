n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
if n==m:
    print(0)
    exit(0)
temp=[]
res=[]
sco=[]
for i in range(n):
    temp.append(i)
for i in range(n):
    if temp[i] not in c :
        res.append(temp[i])
j=0
for i in range(len(res)):
    d=min(abs(res[i]-c[j]) for j in range(len(c)))
    sco.append(d)
print(max(sco))