import sys

N, K = map(int, input().split())
coins = []
res = 0
for _ in range(N):
  coins.append(int(input()))

for i in range(N - 1, -1, -1):
  if K % coins[i] == 0:
    if K == coins[i]:
      res += 1
      K = 0
      break
    elif K < coins[i]:
      continue
    else:
      res += K // coins[i]
      K = K % coins[i]
  else:
    res += K // coins[i]
    K = K % coins[i]
    
  
  if K == 0:
    break

print(res)