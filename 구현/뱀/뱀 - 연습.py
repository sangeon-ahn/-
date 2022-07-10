# 스네이크 게임 만들기
# 보드에는 뱀과 사과가 있음
# 사과를 먹으면 뱀이 1만큼 길어짐
# 시간에 따라 방향을 바꿔야 함
# 게임이 끝나는 시간을 구하기
# 입력값
    # n = 5
    # k = 3
    # 1 3
    # 2 4
    # 3 3
    # l = 3
    # 2 "R"
    # 3 "L"
    # 4 "R"



n = int(input())
k = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]
info = [] # 막힌부분 1. info가 있었다는건 기억했는데 그냥 빈 배열이었는지 초기설정 해줘야 했었는지 헷갈렸다. 근데 여기에 1차원 배열 들어가니까 위에 board처럼 해줄 필요 없다.

for _ in range(k):
    x, y = map(int, input().split()) # 두 수가 입력되었을 때는 map(int, input().split())으로 map으로 감싸준 후, int와 input().split()으로 두 입력받은 수를 스플릿 해준다.
    board[x][y] = 1

l = int(input())

for _ in range(l):
    t, direction = input().split() # 이렇게 두 수를 숫자로 바꾸지 않아야 하는 경우 그냥 input().split() 하면 문자열 형태로 받기 가능
    info.append([int(t), direction]) # 그 후 따로따로 숫자로 바꿔주면 된다.

def turn(currdir, nextdir):
    if nextdir == "L":
        direction = (currdir - 1) % 4 # 동서남북 방향은 4개고 0,1,2,3 값이 필요해서 -1인 경우 나머지 3 나와야 함. 따라서 -1 % 4 = 몫 -1, 나머지 3
    else:
        direction = (currdir + 1) % 4 # 인덱스가 3인 북 방향에서 'R'회전인 경우 인덱스 0 되어야 하고 3 + 1 % 4 = 몫 1 나머지 0
    return direction

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def solution():
    x = 1
    y = 1
    direction = 0
    time = 0
    board[x][y] = 2
    snake = [(x, y)] # 뱀 위치상태를 저장하는 배열인데 생각 못했었다.
    index = 0

    while True:
        # 한 턴마다 계속 위치를 움직이는거라서 while문 안에 있어야 한다.
        nx = x + dx[direction] 
        ny = y + dy[direction]

        # 움직였을 때 게임이 아직 정상인 경우
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                snake.append((nx, ny))

            elif board[nx][ny] == 0:
                board[nx][ny] = 2
                snake.append((nx, ny))
                px, py = snake.pop(0)
                board[px][py] = 0

        # 정상이 아니면 게임 끝
        else:
            time += 1
            break
        
        # 정상이면 위치 갱신하고 지금 시간에 방향 바꾸는지 확인
        x, y = nx, ny
        time += 1

        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time





