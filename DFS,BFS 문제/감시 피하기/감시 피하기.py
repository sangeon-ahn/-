from itertools import combinations

N = int(input())

board = []
blanks = []

for i in range(N):
  board.append(input().split())

  for j in range(N):
    if board[i][j] == 'X':
      blanks.append((i, j))


result = True

def solution(barrierInfo):
  
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  def dfs(x, y):
    global result

    if not result:
      return

    if board[x][y] == "S":
      result = False
      return

    if (x, y) in barrierInfo:
      return;

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < N and ny >= 0 and ny < N:
        if board[nx][ny] == 'X'and not (nx, ny) in barrierInfo:
          board[nx][ny] = 'Checked'

          dfs(nx, ny)
          return

  for i in range(N):
    for j in range(N):
      if board[i][j] == 'T':
        dfs(i, j)

  return result

for (barrierInfo) in list(combinations(blanks, 3)):
  resul = solution(barrierInfo)

  if resul:
    print(resul)
    break

  print(resul)

# 풀이 실패
# 거의 다 했는데 어딘가가 꼬였다.