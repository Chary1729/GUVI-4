c=0
king=input()
for i in king:
  if i.isdigit() or i.isalpha() or re.findall('[r"^@#$%&*)(!"]',i):
    c=c+1
print(c) 
