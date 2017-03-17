
t= int(input())
for a0 in range(t):
    sol=[]
    n,k,b=input().split(' ')
    n,k,b=[int(n),int(k),int(b)]
    min=b*(b+1)/2
    max=b*(2*k-b+1)/2
    if n>=min and n<=max:
        r=(n-min)%b
        q=(n-min)/b
        for i in range(1,b+1):
            sol.append(i)
        #print(sol)
        #print(int(q))
        for i in range(b):
         sol[i]=sol[i]+int(q)
        #print(sol)
        #print(r)
        while(sum(sol)!=n):
            for j in range(len(sol)-1,len(sol)-int(r)-1,-1):
                sol[j]=sol[j]+1
                #print(sol)
            if sum(sol)==n:
                break
        sol=map(int,sol)
        print(*sol,sep=' ')
    else:
        print(-1)

