from collections import defaultdict
n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

for i in alice:
    scores.append(i)

    dic=defaultdict(list)

    scores.sort(reverse=True)
    j=1
    for m in scores:
        if m not in dic.keys():
                dic[m].append(j)
                j=j+1
        else:
            c=int(''.join(map(str,dic.get(m))))
            c=int(c)

            dic[m].append(c)

    #print(dic)
    print(dic[i][0])