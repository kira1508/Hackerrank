a = input().split()
b = input().split()
a = list(map(int,a))
t1 = a
b = list(map(int,b))
t2 = b
final = []
for i in a:
    temp = max(t2)
    if i>temp:
        final.append(i)
    else:
        final.append(temp)
    j = t2.index(temp)
    t2[j] = -1;

print(final)
