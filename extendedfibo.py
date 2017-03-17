
def recur_fibo(n,m):
   """Recursive function to
   print Fibonacci sequence"""
   if n < 1:
       return 0
   elif n==1:
       return 1
   else:
      for i in range(1,m+1):
       return recur_fibo(n-m,m)

c=recur_fibo(5,2)
print(c)