#SOIT108_Base_010
a,b=list(map(int,input().split()))

ans=a//b 
if a%b: ans+= 1

print(ans, end='')