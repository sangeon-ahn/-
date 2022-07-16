from collections import deque

N, K = map(int, input().split())
data = []
virus_data = []

for i in range(N):
  data.append(list(map(int, input().split())))

  for j in range(N):
    if data[i][j] != 0:
      virus_data.append((data[i][j], 0, i, j))

S, X, Y = map(int, input().split())

virus_data.sort()

q = deque(virus_data)
print(data, virus_data, q)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
  virus, time, x, y = q.popleft()

  if time == S:
    print(data[X - 1][Y - 1])
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and nx < N and ny >= 0 and ny <N:
      if data[nx][ny] == 0:
        data[nx][ny] = virus
        q.append((virus, time + 1, nx, ny))

# 문제 이해하고 문제 풀이도 이해한 다음에 밥먹고 나서 시간 지난 후 풀어봤는데 
# 잘 이해해서 그런지 두번째 시도만에 됐다. 
