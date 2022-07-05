# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(two_dimension_list):
    row_length = len(two_dimension_list)
    column_length = len(two_dimension_list[0])
    result = [[0] * row_length for _ in range(column_length)] # 2차원 배열 만드는 법, [[0]* n for _ in range(m)]
    
    for i in range(row_length):
        for j in range(column_length):
            result[j][row_length - i - 1] = two_dimension_list[i][j] # 이해 안되는 부분 1
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    #새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j] # 이해 안되는 부분 2
    
    # 4가지 방향에 대해 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 확인
                if check(new_lock) == True:
                    return True
                
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))

# 이해 안되는 부분 해결
    # 1번: 회전한 2차원 배열의 행값은 회전 전 열값과 같다. 회전한 2차원 배열의 열값은 배열 행 길이에 회전 전 행값+1을 뺀 값과 같다.
    # 2번: 0으로 초기화한 3배 크기 자물쇠 만들고 가운데에 기존 자물쇠 넣어야 하니까 (n, n)부터 시작하게 한다.

# 키포인트
    # 1. 자물쇠 * 3 하고 열쇠가 모든 경우의 수를 돌면서 확인한다.
    