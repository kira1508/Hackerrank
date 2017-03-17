t= int(input())
for a0 in range(t):
    flag= True
    s=input().strip()
    s1=input().strip()
    for i in s:
        if i in s1:

            flag=False
    if flag:
        print("NO")
    else:
        print("YES")