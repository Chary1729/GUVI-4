import re
count=counts=0
strings=input()
for i in strings:
  if(i.isalpha()==True):
    count=count+1
for j in strings:
  if re.findall('["^@#$%&*)(!"]',j):
    counts=counts+1
if(count==0):
  print(counts)
elif(counts==0):
  print(count)

