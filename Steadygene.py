n=int(input())
res=list(map(list,input().strip()))
temp=[]
even=[]
odd=[]
a=res.count('A')
if a<=2:
 temp.append(a)
c=res.count('C')
if c<=2:
 temp.append(c)
t=res.count('T')
if t<=2:
 temp.append(t)
g=res.count('G')
if g<=2:
 temp.append(g)

for i in range(len(temp)):
    if temp[i]%2==0:
        even.append(temp[i])
    else:
        odd.append(temp[i])





