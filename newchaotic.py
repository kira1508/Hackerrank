t = int(input())
for a0 in range(0,t):
    sum=0
    flag = True
    n=int(input())
    b=list(map(int,input().split(' ')))
    for i, j in enumerate(b):
        if(j-1)-i > 2:
            print("Too choatic")
            flag=False
            break

    if flag:
     for i in range(0,len(b)-1):
        for j in range(0,len(b)-1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                sum=sum+1

    if flag:
     print(sum)