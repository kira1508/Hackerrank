import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
res=[]
topic_i = 0
f=0
g=0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)
a=str(0)
a=int(a,2)
a=str(a)
for i in range(n):
 for j in range(i+1,n):
     c=format(int(topic[i],2)|int(topic[j],2),'b')
     if c>=a:
         a=c
         res.append(a)


b=max(res)
print(b.count('1'))
for i in res:
    if str(i)==str(b):
        f=f+1
print(f)

