from functools import reduce

t=int(input())
s1=int(input())
s2=int(input())
k=int(input())
n=int(input())
n=n+1
i=1
tax=[]
temp=[]
tax=list(map(float, tax))
temp= list(map(float, temp))
tax.append(t)
tax.append(t)

for i in range(2,s1+2):
    tax.append(i)
c=tax[-1]
if(n-1>c):
 for i in range(c,s2+c):
    tax.append(2*tax[i])

 #print(tax)
 m=len(tax)
 #print(m)
 for i in range (m,n):
    temp=[]
    temp= list(map(float,temp))
    temp=tax[-k:]
    d=reduce(lambda x, y: x*y, temp)
    tax.append(d)
 del tax[0]
 print(tax)
 print(tax[-1]%100000007)
else:
    print(tax[k])