n,k=input().split(' ')
n,k=[int(n),int(k)]
l=[]
t=[]
imp=[]
non=[]
sum=0
flag=0
for a0 in range(n):
  temp,temp1=input().split(' ')
  temp,temp1=[int(temp),int(temp1)]
  l.append(temp)
  t.append(temp1)
for i in range(len(t)):
  if t[i]==1:
      imp.append(l[i])
      flag=1
  else:
      non.append(l[i])

imp.sort()
imp.reverse()
if k>=len(imp):
    k=len(imp)
if flag==1:
    for j in range(k):
        sum=sum+imp[j]
#print(sum)
for i in range(len(non)):
    sum=sum+non[i]

for m in range(k,len(imp)):
    sum=sum-imp[m]

print(sum)


