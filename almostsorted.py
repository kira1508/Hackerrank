
t= int(input())
l=0
a = list(map(int, input().strip().split(' ')))
b=list(a)
x=list(a)
for i in range(len(a)):
    if a[i]>a[i+1]:
        l=i
        break
b=a[l:]
c=min(b)
d=a.index(c)
a[l],a[d]=a[d],a[l]
if(all(a[j] <= a[j+1] for j in range(len(a)-1))):
    print("yes")
    print("swap "+str(l+1)+" "+str(d+1))
    exit(0)
else:
    g=x[l:d+1]
    g.reverse()
    h=x[0:l]+g[0:]+x[d+1:]
    if(all(h[j] <= h[j+1] for j in range(len(h)-1))):
        print("yes")
        print("reverse "+str(l+1)+" "+str(d+1))
        exit(0)
    else:
        print("no")

