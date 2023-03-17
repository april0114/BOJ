a = []

for _ in range(10):
  b = int(input())
  c = b % 42
  a.append(c)

s = set(a)
print(len(s))
