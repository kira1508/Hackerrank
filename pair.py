m, n = map(int, input().strip().split(' '))
b=input().split(' ')
b=list(map(int,b))
b.sort()
#print(b)
c=0
j=m-1
i=0
while(i<m and i<=j):
     #print(abs(b[i]-b[j]))
     if abs(b[i]-b[j])!=n:
        j=j-1
     else:
        c=c+1
        i=i+1
        j=m-1
     if i==j:
         i=i+1
         j=m-1


print(c)


