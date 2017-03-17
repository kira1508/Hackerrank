m, n = map(int, input().strip().split(' '))
b=input().split(' ')
b=list(map(int,b))
c=0
#print(len(set(b)))
print( set(b) & set(x + n for x in b))