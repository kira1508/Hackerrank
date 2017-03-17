t = int(input())
a = list(map(int, input().strip().split(' ')))
a.sort()
min=0
print(a)
for i  in range(0,len(a)-1):
    for j in range(i+1,len(a)-1):
        if a[j]-a[i]>min :
            min= a[j]-a[i]
            print(str(a[j])+' '+str(a[i]))
        else:
            continue