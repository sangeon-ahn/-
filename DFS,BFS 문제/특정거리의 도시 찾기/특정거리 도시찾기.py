from collections import deque
from typing import Deque
from collections import deque;

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