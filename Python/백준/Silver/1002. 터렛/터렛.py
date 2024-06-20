import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if x1 == x2 and y1 == y2:  # 두 원의 중심이 같은 경우
        if r1 == r2:  # 반지름도 같은 경우
            print(-1)  # 무한개의 교점
        else:
            print(0)  
    else:
        if (r1 + r2) == d or abs(r2 - r1) == d:  # 외부에 속하거나 내부에 속하는 경우
            print(1)
        elif abs(r1 - r2) < d < (r1 + r2):  # 두 원이 두 점에서 만나는 경우
            print(2)
        else:
            print(0)  # 그 외의 경우 (교점 없음)
