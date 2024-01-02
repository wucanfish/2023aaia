#SOIT106_BASE_008
a=list(map(int,input().split()))
if a[0]>a[1] :
	a[0],a[1]=a[1],a[0]

for i in range(a[0],a[1]+1):
	if i%5==0 :
		print(i) 