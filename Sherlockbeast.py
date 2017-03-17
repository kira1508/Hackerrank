t=int(input())
for a0 in range(t):
    flag=0
    n=int(input())
    n1=n
    a=[]
    l=0
    if n<3 or n==7 or n==4:
        print(-1)
        continue
    if n1%3==0 and n1%5==0:
       print(str(5)*int((n1)))
       continue
    while(n%3!=0 and n>=5):
        n=n-5



    l=n1-n
    a.append(str(5)*n)
    a.append(str(3)*l)
    print(*a,sep="")

