t =int(input())
w=list(map(int,input().split(' ')))
w.sort()
a=[arr+4 for arr in w]
c=0
le=0
#print(a)
#print(w)
j=0
i=0
while(i<t):
    if w[i]<=a[j]:
        c=c+1
        #print(str(w[i])+' '+str(a[j]))
        i=i+1
    else:
        #print(str(w[i])+' '+str(a[j]))
        #print(c)
        if c<=5 and c>0:
            le=le+1
        c=0
        j=j+1
i=i-1
if w[i]<=a[i]:
 print(le+1)
else:
    print(le)
#print(j+1)
