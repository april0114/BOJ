N = int(input())
meetings = []

for _ in range(N):
    s_t, e_t = map(int, input().split())
    meetings.append((e_t, s_t))

# 종료 시간을 기준으로 정렬
meetings.sort()

count = 0
end_time = 0

for e_t, s_t in meetings:
    if s_t >= end_time:
        count += 1
        end_time = e_t

print(count)