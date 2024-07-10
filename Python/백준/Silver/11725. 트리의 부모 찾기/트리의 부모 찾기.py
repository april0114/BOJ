import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
#인접 노드 리스트를 저장할 리스트
verticies = [[0]for _ in range(N+1)]
#각 노드의 부모를 저장할 리스트 초기화
parent = [0] *(N+1)

#트리의 간선은 N-1개로 이루어져 있으므로 반복
for _ in range(N-1):
    a,b = map(int,input().split())
    verticies[a].append(b)
    verticies[b].append(a)

parent[1] = 0
q = deque()
#루트 노드인 1번 노드의 부모를 0 으로 설정
q.append(1)

#큐가 빌 때 까지 반복
while q:
    #큐의 가장 앞에 있는 노드를 꺼내 현재 노드로 설정
    current = q.popleft()
    #현재 노드에 인접한 모든 노드를 순회
    for v in verticies[current]:
        if parent[v] == 0:
            parent[v] = current
            q.append(v)
print('\n'.join(map(str,parent[2:])))
