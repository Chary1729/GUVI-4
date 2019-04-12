count=0
f=1
s=1
a=[]
l=int(input())
a.append(f)
a.append(s)
for i in range(1,l-1):
  n=f+s
  f=s
  s=n
  a.append(n)
print(*a,end=" ")

  
