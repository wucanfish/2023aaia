#SOIT108_Advance_007
a=list(map(int,input().split()))

for i in range(len(a)):
	if a[i]==min(a) :
		ans=i+1
		break
print(ans,int(1.2*3600/min(a)))