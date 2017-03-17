
n = int(input().strip())
tot=[]
tem=[]
c=0
for i in range(0,n):
    tem=input()
    tot.append(tem)
n1=int(input())
for i in range(0,n1):
    tem=input()
    c=tot.count(tem)
    print(c)