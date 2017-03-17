t = int(input())
for a0 in range(t):
    m=int(input())
    f=int(input())
    cos = list(map(int, input().strip().split(' ')))
    cos = [0]+cos
    for i in range(1,f+1):
        for j in range(i+1,f+1):
            if(cos[i]+cos[j]==m):
                print(str(i)+' '+str(j))
                break



