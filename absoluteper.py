t = int(input())
for a0 in range(t):
     flag=0
     a=[]
     c=0
     n,k=input().split(' ')
     n,k= [int(n),int(k)]
     for i in range(1,n+1):
        a.append(i)
     print(*a,sep=' ')
     b=list((x-k) for x in a)
     #print(b)
     for i in range(len(a)):
         #print(str(a[i])+' '+str(b[i]))
         if a[i]-b[i]==k:
             #print('yes')
             if i==len(a)-1:

              flag=1


     if flag:
         for m in range(len(b)):
             if b[m]>0:
                 c=m
                 break

         res=a[c:]+a[:c]
         print(*res,sep=' ')
         if all(abs(res[i]-a[i])==k for i in range(len(a))):
             print(*res,sep=' ')
         else:
             print(-1)


     else:
         print(-1)
