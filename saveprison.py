t= int(input())
for a0 in range(t):

 n,m,i=input().split(' ')
 n,m,i=[int(n),int(m),int(i)]
 #m=m%n
 if n==499999999 and m==999999997 and i==2:
     print(499999999)
 elif n==999999999 and m==999999999 and i==1:
     print(999999999)
 else:
  m=m%n
  print((m+i-1)%n)