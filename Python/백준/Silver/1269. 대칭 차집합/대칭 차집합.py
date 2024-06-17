a, b = map(int,input().split())

c = list(map(int, input().split()))
d = list(map(int, input().split()))

set_c = set(c)
set_d = set(d)

len_c = set_c - set_d
len_d = set_d - set_c

e = len(len_c)
f = len(len_d)

sum = e + f
print(sum)