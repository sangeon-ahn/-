# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

from itertools import combinations

N, M = map(int, input().split())

chicken = []
house = []

def getSum(candidate):
  result = 0

  for hx, hy in house:
    temp = 1e9

    for cx, cy in candidate:
      temp = min(temp, abs(cx - hx) + abs(cy - hy))

    result += temp

  return result

def solution():
  for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
          house.append((i, j))
        elif row[j] == 2:
          chicken.append((i, j))

  candidates = list(combinations(chicken, M))

  temp = 1e9

  for candidate in candidates:
      temp = min(temp, getSum(candidate))

  return temp

print(solution())

# 치킨집 중 M개를 골라서 치킨거리가 최소인 경우를 구하는 문제
# M개를 고르는 방법: 조합, itertools의 combination 사용
# 각각의 경우의 수에 대항하여 치킨거리를 구해야 함
# 하나의 집은 M개의 치킨집 중 가장 최단거리의 치킨집을 골라서 사먹음
# 따라서 모든 치킨집을 순회하며 가장 작은 거리인 경우일 때를 더해주면 됨

# 어려웠던 부분
  # 1. for문 중첩해서 house랑 chicken안에 넣어줄 때 row를 어디에 선언할 지, 조건식은 어떻게 세울 지
  # 2. combination이 생각이 안나고 collections가 생각났다.
  
