n = [1, 1, 2, 2, 2, 8]
l = list(map(int, input().split())) #입력받기

for i in range(6):
  print(n[i] - l[i], end=' ')
