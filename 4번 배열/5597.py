N = 28
list1 = []
for i in range(N):
  list1.append(int(input()))
  list1.sort()

for i in range(1,N+1):
  if i not in list1:
    print('%d' % i)
