n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
min=100000000007
a.sort()
i=0
c=0
j=i+1
while i<=j and j<n:
   c=abs(a[i]-a[j])
   #print(c)
   if min>c and c>0:
       min=c
       #print(c)
       if j==len(a)-1:
        i=i+1
       else:
           j=j+1
   else:
       if i==j:
           j=j+1
       else:
        i=i+1

if min==100000000007:
   print(0)
else:
 print(min)