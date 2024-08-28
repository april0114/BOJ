n, m = map(int,input().split())
coins = []
count = 0
for _ in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)

for coin in coins:
    count += (m//coin)
    m %= coin
print(count)