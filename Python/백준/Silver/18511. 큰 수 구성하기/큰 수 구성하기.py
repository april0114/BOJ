from itertools import product

# 입력 처리
N, K_count = map(int, input().split())
K = list(map(int, input().split()))

# N의 자릿수를 구합니다.
N_str = str(N)
N_length = len(N_str)

# 가장 큰 수를 저장할 변수
largest_number = 0

# 가능한 모든 자릿수 조합을 만듭니다.
for length in range(1, N_length + 1):
    for combo in product(K, repeat=length):
        num_str = ''.join(map(str, combo))
        num = int(num_str)
        if num <= N:
            largest_number = max(largest_number, num)

print(largest_number)
