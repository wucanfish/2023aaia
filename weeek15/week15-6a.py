#SOIT108_Base_004
a=list(map(int,input().split()))

if a[0]>1 and a[1]>1 :
	ans=1
if a[0]<1 and a[1]>1 :
	ans=2
if a[0]<1 and a[1]<1 :
	ans=3
if a[0]>1 and a[1]<1 :
	ans=4
print(ans) 
       
 