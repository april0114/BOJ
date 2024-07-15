from itertools import permutations

N,M = map(int,input().split())
arr = list(range(1, N+1))

perm = permutations(arr,M)
for p in perm:
    print(' '.join(map(str, p)))