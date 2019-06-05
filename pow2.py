x=int(input())
def isPowerOfTwo (x):
  return (x and (not(x & (x - 1))) ) 
if(isPowerOfTwo(x)): 
	print('yes') 
else: 
	print('no') 
	
