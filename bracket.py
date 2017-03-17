t = int(input().strip())
for a0 in range(t):
    b=[]
    d=[]
    c=0
    a = input().strip()
    n=len(a)
    #print(n)
    l=int(n/2)
    for i in range(0,n):
        if(a[i]=='(' or a[i]=='[' or a[i]=='{'):
         b.append(a[i])


    #print(b)
    j=0
    for i in range(l,n):

        print(d[j] + b[i])
        if((b[i]==')'and d[j]=='(') or (b[i]==']'and d[j]=='[') or (b[i]=='}'and d[j]=='{')):
            c=c+1
            #print(c)
        j=j+1
    if(c==l):
         print('YES')
    else:
         print('NO')