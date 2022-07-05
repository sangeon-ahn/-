# 90도 회전 함수 제작
# 잘 맞물렸는지 체크하는 함수 제작
# 메인 함수 제작

def rotate_90_degree(key):
    n = len(key)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = key[i][j]
    
    return result

def check(lock):
    lock_length = len(lock) // 3
     
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if lock[i][j] != 1:
                return False
    
    return True

def solution(key, lock):
    lock_length = len(lock)
    key_length = len(key)
    new_lock = [[0] * (lock_length * 3) for _ in range(lock_length * 3)]

    for i in range(lock_length):
        for j in range(lock_length):
            new_lock[lock_length + i][lock_length + j] = lock[i][j]

    for rotation in range(4):
        key = rotate_90_degree(key)
        for x in range(lock_length * 2):
            for y in range(lock_length * 2):
                for i in range(key_length):
                    for j in range(key_length):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                
                for i in range(key_length):
                    for j in range(key_length):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))