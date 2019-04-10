import statistics
x=int(input())
lis=[int(i) for i in input().split()]
lis.sort()
print(statistics.median(lis))
