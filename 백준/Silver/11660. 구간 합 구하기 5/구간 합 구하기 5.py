import sys
input = sys.stdin.readline;


N, M = map(int, input().split());

mat = [list(map(int, input().split())) for i in range(N)]

prefix = [[0]* N for _ in range(N)]

for i in range(N):
  sum_ = 0
  for j in range(N):
    sum_ += mat[i][j]
    prefix[i][j] = sum_




for i in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  sum_ = 0
  if y1 != 1:
    for j in range(x1, x2 + 1):
      sum_ += prefix[j - 1][y2 - 1] - prefix[j - 1][y1 -2]
  else:
    for j in range(x1, x2 + 1):
      sum_ += prefix[j - 1][y2 - 1]
  
  print(sum_)
	