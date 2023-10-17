a=input()
b=int(a)
if b>=90:
	ans='A'
elif 80<=b<90:
   		ans='B'
elif 70<=b<80:
	ans='C'
elif 60<=b<70:
	ans='D'
else:
	ans='F'	
print(ans, end='')