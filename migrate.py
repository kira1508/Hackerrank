import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
max=0
for i in range(1,6):
    c=types.count(i)
    if max<c:
        max=c
print(max)