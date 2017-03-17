from collections import Counter
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
s={}
l=0
x=Counter(magazine)
y=Counter(ransom)

t=sum((y-x).values())
if(t==0):
    print("Yes")
else:
    print("no")

