a=list(map(int,input().split()))

ans=1
print('Enter the number of values to be processed: ', end='')
for i in range(1, a[0]+1):
	print('Enter a value: ', end='')
	ans *=a[i]
	
print('Product of the', a[0], 'values is' , ans , end='')