a = 120 
# 1 2 3 4 5 6 10.......
ans = 0
for i in range(1,a+1):  # 包含1......a本身
  if a%i== 0:
    print(i , end=' ')
    ans += 1
print('有幾個整除?',ans)