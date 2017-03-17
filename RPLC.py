t=int(input())
for a0 in range(0,t):
    sum=0
    flag=0
    i=0

    k=1
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    while(1):
        #print(i)
        sum=sum+a[i]
        #print(sum)
        if(sum<=0 and flag==0):
            flag=1
            l=abs(sum)
            #print(l)
            l=l+1
            a=[l]+a
            i=0
            #print(a[0])
            sum = 0
            #print(sum)
        if(sum<=0 and flag==1):
            del a[0]
            l=l+1
            a=[l]+a
            i=0
            #print(a)
            sum=0
        if sum>0 and i==len(a)-1:
            if(flag==0):
                print(l+1)
            else:
             print(l)
            break

        if sum>0:
            i=i+1
