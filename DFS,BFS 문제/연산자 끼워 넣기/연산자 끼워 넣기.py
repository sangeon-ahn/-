# from itertools import product

# n = 4
# print(list(product(['+', '-', '*', '/'], repeat=(n - 1
# ))))

n = int(input())
numbers = list(map(int, input().split()))
[plus, minus, mul, div] = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

def dfs(i, number):
  global plus, minus, mul, div, max_num, min_num
  if i == n:
    max_num = max(max_num, number)
    min_num = min(min_num, number)

    return

  else:
    if plus > 0:
      plus -= 1
      dfs(i + 1, number + numbers[i])
      plus += 1
    
    if minus > 0:
      minus -= 1
      dfs(i + 1, number - numbers[i])
      minus += 1
    
    if mul > 0:
      mul -= 1
      dfs(i + 1, number * numbers[i])
      mul += 1

    if div > 0:
      div -= 1
      dfs(i + 1, int(number / numbers[i]))
      div += 1
    
dfs(1, numbers[0])

print(max_num, min_num)

# dfs문제는 탐색하는 과정이 머릿속에 그려져야 한다.
# 지금 문제는 dfs과정이 복잡하다. 잘 그려지지 않는다.
# 그래도 저 dfs의 결과가 중복순열이라는건 안다.
# 따라서 중복순열을 구현하기 위해서는 각각의 경우에 dfs를 둔 후, dfs호출문을 인덱스의 -와 +문 사이에 두면 중복순열이 된다.