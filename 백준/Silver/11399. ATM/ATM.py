N = int(input())

P = list(map(int, input().split()))
P.sort()

sum_ = 0
for i in range(N):
  sum_ += sum(P[0:i + 1])

print(sum_)