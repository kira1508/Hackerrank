t=int(input())

for a0 in range(0,t):
 c=0
 b=[]
 l=0
 n=int(input())
 a = list(map(int, input().strip().split(' ')))
 b=a
 for i in range(0,len(a)-2):
    temp= a[i:i+3]
    #print(temp)


    if(all(temp[j] <= temp[j+1] for j in range(len(temp)-1))):
            if(len(a)==3):
                print("Yes")
                break
            else:
                continue
    else:

            for j in range(1,4):
                res=temp[j:]+temp[:j]
                #print(res)
                a[i:i+3]=res
                print(a)
                if(all(a[j] <= a[j+1] for j in range(len(a)-1)) or all(a[j+1] <= a[j] for j in range(len(a)-1)) ):
                    print("YES")
                    c=1
                    break
                if(j==3 and i!=len(a)-3):
                    a=b
                #print(len(a)-2)
                if(j==3 and i==len(a)-3):
                    print("NO")





