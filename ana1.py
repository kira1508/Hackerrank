import itertools
ana=[]
t=[]
for i in itertools.permutations(input(),3):
    t=''.join(i)
    ana.append(t)
ana.sort()
print(*ana,sep=' ')