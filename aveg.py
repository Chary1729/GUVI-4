sum=0
num=int(input())
num1=[int(num1) for num1 in input().split()]
while(sum<len(num1)):
  for i in num1:
    sum=sum+i
j=int(sum)/len(num1)
j=int(j)
print(j)
