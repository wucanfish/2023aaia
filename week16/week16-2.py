s = '00111'
N=len(s)
ans=0 
for left in range(N-1):
  print('left',left, 'i<=left 有誰?' ,end=' ')
  for i in range(N):
    if i<=left: print(s[i], end=' ')#把i<=left 印出來
  print('i>left有誰?',end=' ')
  for i in range(N):
    if i >left: print(s[i], end=' ')#把i>left 印出來
  
  print()