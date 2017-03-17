
q = int(input().strip())
for a0 in range(q):
    c=0
    n = int(input().strip())
    sizes = list(map(int, input().strip().split(' ')))
    v = int(input().strip())
    for a1 in range(v):
        smallest,largest = input().strip().split(' ')
        smallest,largest = [int(smallest),int(largest)]
        if sizes.count(-1)!=len(sizes):
            for i in range(len(sizes)):
                if sizes[i]>=smallest and sizes[i]<=largest:
                    #print(sizes[i])
                    c=c+1
                    sizes[i]=-1

    print(c)
