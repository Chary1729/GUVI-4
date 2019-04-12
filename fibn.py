count=0
f=1
s=1
a=[]
l=int(input())
if l==1:
  a.append(l)
else:
  a.append(f)
  a.append(s)
for i in range(1,l-1):
  n=f+s
  f=s
  s=n
  a.append(n)
print(*a)

  
