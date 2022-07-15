N, M = map(int ,input().split())
data = []
temp = [[0] * M for _ in range(N)]

for i in range(N):
  data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and nx < M and ny >= 0 and ny < N:
      if temp[nx][ny] == 0:
        temp[nx][ny] == 2
        virus(nx, ny)

def check():
  result = 0

  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        result += 1

  return result

def dfs(count):
  global result

  if count == 3:
    for i in range(N):
      for j in range(M):
        temp[i][j] = data[i][j]

    for i in range(N):
      for j in range(M):
        if temp[i][j] == 2:
          virus(i, j)

    result = max(result, check())
    return

  for i in range(N):
    for j in range(M):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)

# 알게된 점
  # 1. dfs 오랜만이라 어려웠다.
  # 2. dfs count == 3 될 때까지 벽 세우다가 3 되면 temp 리스트에 데이터 넣고 바이러스 번식한 후, 0 개수 세는 함수에 넣어서 구한다. dfs의 if문에서는 return을 해줘야 무한 재귀에서 나올 수 있다. 나오게 되면 dfs호출문 다음 줄로 가게되고 여기서 모든 칸들 돌아야하기 때문에 다시 값을 0으로 해주고 count도 1을 빼준다.