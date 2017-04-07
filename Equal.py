t=int(input())

for a0 in range(t):
    n=int(input())
    choc=list(map(int,input().split(" ")))
    k=min(choc)
    i=0
    num=0
    MIN=99999999
    res=[]
    #print(k)
    fin=0
    while( k>=0):
        res=[]
        for j in range(n):
            c=choc[j]-k
            res.append(c)
        fin=0
        #print(res)
        for m in range(len(res)):

            num=res[m]
            a=int(num/5)
            b=int((num%5)/2)
            c=int(((num%5)%2)/1)
            fin+=a+b+c
           #print(fin)
        if(fin <MIN and fin>0):
            MIN=fin
            #print("Inside min "+str(fin))


        k=k-1

    print(MIN)

