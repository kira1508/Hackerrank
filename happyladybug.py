from collections import Counter
Q = int(input().strip())
for a0 in range(Q):
    m=0
    flag=0
    n = int(input().strip())
    b = list(input().strip())
    a=list(b)
    c=b.count('_')
    if c==0 and len(set(b))>1:

        if all(a[i]==a[i+1] for i in range(len(a))):
                print("YES")
                continue
        i=0
        j=i+1
        while(j<=len(a)):
            if a[i]==a[j]:
                m=m+1
            i=i+2
            j=j+2
        #print(m)
        if m==len(a)/2:
            print("YES")
            continue

        print("NO")
        continue

    for i in range(len(b)):
        if b[i]=='_':
            a.remove(b[i])
            #print(a)
    #le=len(b)-c
    #print(a)
    x=Counter(a)
    res=x.values()
    for i in res:
        if i==1:
            print('NO')
            flag=1
            break


    if flag==0:
        print('YES')