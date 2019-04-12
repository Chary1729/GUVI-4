a,b=input().split()
if(a.isdigit()==True and b.isdigit()==True):
  a=int(a)
  b=int(b)
  
def swap(a,b):
  if(a>0 and b>0):
    (a,b)=(b,a)
    print(a,b)
swap(a,b)
 
  
