
t= int(input())
for a0 in range(0,t):
 a = list(input().strip())
 b=list(a)
 a.reverse()
 c=0
#print(ord(b[0])-ord(a[0]))
 for i in range(0,len(b)-1):
    if(abs(ord(b[i])-ord(b[i-1]))==abs(ord(a[i])-ord(a[i-1]))):

        c=c+1
        if(c==len(b)-1):
            print("funny")
    else:
        print("not funny")
        break

