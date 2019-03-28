mylist=[]
l,h=input().split()
if(l.isdigit()==True and h.isdigit()==True):
  l=int(l)
  h=int(h)
  for i in range(l,h):
    sum=0
    temp=i
    while(temp>0):
      digit=temp%10
      sum+=digit**3
      temp//=10
    if(i==sum):
      mylist.append(i)
      king=len(mylist)
  for j in range(king-1):
    print(mylist[j],end=" ")
  print(mylist[king-1])  
      
