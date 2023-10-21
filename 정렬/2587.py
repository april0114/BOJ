b=[]

for i in range(5):
    a = int(input())
    b.append(a)

    result = sum(b)
    b.sort()
mean = result//len(b)

print(mean)
print(b[2])
