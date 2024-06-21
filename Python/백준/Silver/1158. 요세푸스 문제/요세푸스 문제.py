N , K= map(int, input().split())

survive = list(range(1, N+1))
dead = []
index = 0

while survive:
    index = (index+K-1) % len(survive)
    dead.append(survive.pop(index))

print("<", ", ".join(map(str, dead)), ">", sep='')