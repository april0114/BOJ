N = 9
list1 = []
for i in range(N):
  list1.append(int(input()))

print(max(list1))
print(list1.index(max(list1)) + 1)
