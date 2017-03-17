from functools import reduce
n = int(input())
a = list(map(int, input().strip().split(' ')))
max=0
sum=0
for k in range(len(a)):
 sum = 0
 res = a[k:]+a[:k]
 print(*res,sep='')
 for i in range(0,len(res)):
     sum=sum+res[i]*i

 if(max<sum):
     max=sum

print(max)