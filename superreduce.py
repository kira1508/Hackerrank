from collections import Counter

res=input()
x=Counter(res)
val=list(x.values())
y={}
y=dict(x)
for i,j in x.items():
    if j%2==0:
       del y[i]
print(''.join(list(sorted(y.keys()))))
