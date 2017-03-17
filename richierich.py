import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
number = input().strip()
print(number)
j=len(number)-1
i=0
while(i<n and j>=i and k>=0):
   if number[i]==number[j]:
       i=i+1
       j=j-1

       continue
   else:
    if(number[i]!=9 and number[j]!=2):
        number[i]=9
        number[j]=9
        k=k-2
        i=i+1
        j=j-1
    if(number[i]==9 and number[j]!=9):
        number[j]=9
        k=k-2
        i=i+1
    if(number[j]==9 and number[i]!=9):
        number[i]=9
        k=k-2



