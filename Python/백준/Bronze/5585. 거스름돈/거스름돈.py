N = 1000
coins = [500,100,50,10,5,1]
minus = int(input())
change = 0
changes = N-minus

for coin in coins:
    change += (changes//coin)
    changes %= coin

print(change)