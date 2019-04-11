import re
c=0
king=input()
for i in king:
  if re.search('[r"^@#$%&*)(!,><;"_".":"]',i):
    c=c+1
print(c) 
