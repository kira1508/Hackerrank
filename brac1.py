t = input().strip()
t1= input().strip()
res = []
c=0
k=0
l=len(t1)

for i in range(0,len(t)-l+1):
    res=t[i:i+l]

    for i in res:
        if i in t1:
           c=c+1

        if c==l and res!=t1:
            k=k+1


    c=0

print(k)