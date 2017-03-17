t=int(input().strip())
c=0
s={}
s1={}
for i in range(0,t):
    s[i]=input().strip()
t1=int(input().strip())
for i in range(0,t1):
    s1[i]=input().strip()

share=list(set(s.values()) &set( s1.values()))
print(share)
for i in  range(0,len(share)):
    for j in range(0,t):
        if str(share[i])==s.get(j):

         c=c+1
    print(c)
    c=0
