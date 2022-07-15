from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
  a,b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque([X])

while q:
  now = q.popleft()
  for city in graph[now]:
    if distance[city] == -1:
      distance[city] = distance[now] + 1
      q.append(city)

for a, b in enumerate(distance):
  if b == K:
    print(a)


# 알게된 점
  # 1. graph의 인덱스를 도시 번호로 지정하기 위해 N + 1개의 원소를 graph에 만들었다.
  # 2. 큐 자료구조로 거리를 구할 때 이전 도시까지의 거리 + 1 하면 된다. 학교에서 배운거다.