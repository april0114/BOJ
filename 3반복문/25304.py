sum = 0
X = 총금액
N= int(input('구매한 물건의종류 수'))
for i in range(N):
  a, b = map(int, input().split())
  sum += (a*b)

if sum == X:
  print('yes')
else : 
  print('no')
