#SOIT108_Advance_011
a=int(input())
hh=a//3600
mm=a//60%60
ss=a%60


print(f'{hh:02d}:{mm:02d}:{ss:02d}',end='') 
       