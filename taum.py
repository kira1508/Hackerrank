
t = int(input().strip())
for a0 in range(t):
    flag=0
    res1=0
    res=0
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    cosb=b*x
    cosw=w*y
    temp=b*z
    temp1=w*z
    #print(cosb)
    #print(cosw)
    #print(temp)
    #print(temp1)
    res2=cosw+cosb
    #print(res2)
    if cosb>temp and cosw>temp1:
        cosb=temp
        cosw=(b+w)*y
        res1=cosb+cosw
        cosw=temp1
        cosb=(b+w)*x
        res=cosb+cosw
        #print(res)
        #print(res1)
        if res1>res:
            if res<res2:
             print(res)
            else:

                print(res2)

        else:
            if res1<res2:
             print(res1)
            else:
                print(res2)
        continue
    if cosb>temp:
        cosb=temp
        cosw=(b+w)*y
        res1=cosb+cosw
        if res1<res2:

        #print(cosw)
        #print(cosb)
          print(res1)
        else:
            print(res2)
        continue
    if cosw>temp1:
        cosw=temp1
        cosb=(b+w)*x
        res=cosb+cosw
        if res<res2:
            print(res)
        else:
            print(res2)
        continue
    if flag==0:
        print(cosb+cosw)
