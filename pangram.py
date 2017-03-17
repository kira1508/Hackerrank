a=str(input().strip(' '))
#print(a)
a=a.lower()
a=set(a)
#print(a)
#print(len(a))

if len(a)-1==26:
    print("pangram")
else:
    print("not pangram")