t =int(input())
for a0 in range(t):
    n,m=input().split(' ')
    n,m= [int(n),int(m)]
    n=n%1000000007
    m=m%1000000007

    c=0
    a=[]
    a.append(0)
    a.append(1)
    d=0
    e=1
    if m<=n+1:
        for i in range(m-2):
            f=pow(2,i)%1000000007
            a.append(f)


        #e=pow(2,d+1)
        #a.append(e)
        #h=pow(2,d+2)
        #a.append(h)
        print(a)
        if len(a)<n+1:
            d=sum(a[-m:])
            a.append(d)
            for j in range(n-m):
                e=a[-1]-a[j]%1000000007
                c=e+a[-1]%1000000007
                a.append(c)
            print(a)

    else:
        for i in range(n-1):
         f=pow(2,i)%1000000007
         a.append(f)
    print(a[-1])