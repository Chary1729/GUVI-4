minutes=int(input())
hours=minutes//60
if(hours==0):
  minutess=minutes
else:
  minutess=minutes%60
print(hours,minutess)
