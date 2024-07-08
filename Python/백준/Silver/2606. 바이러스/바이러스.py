from collections import deque
# 컴퓨터의 수
a = int(input())
# 네트워크 상에서 직접 연결 되어있는 컴퓨터 쌍의 수
b = int(input())
visit = [0] * (a+1)
# 그래프
graph = [[] for _ in range(a+1)]

for i in range(b):
    c,d = map(int,input().split())
    #양방향으로 
    graph[c] += [d]
    graph[d] += [c]
visit[1] = 1

Q = deque([1])
#Q가 비어있지 않는 동안
while Q:
    e = Q.popleft()
    for j in graph[e]:
        #방문되지 않았다면
        if visit[j] == 0:
            Q.append(j)
            visit[j] = 1
print(sum(visit)-1)
