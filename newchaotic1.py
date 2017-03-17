t = int(input().strip())
for a0 in range(t):
    flag=False
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    res=[]
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

    for i in range(0,R-r):
        for j in range(0,C-c):
            for k in range(r):
                for l in range(c):
                    print(P[k][l],end='')
                    if G[i+k][j+l] == P[k][l]:
                        flag==True




              #res.append(G[i+k][j+l])
                print('\n')

    if flag:
        print("YES")





                #print("\n")

            #res=G[k][l]


    #print(res)

