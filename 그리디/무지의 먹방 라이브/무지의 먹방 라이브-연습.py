import heapq


food_times = [3, 1, 2]
k = 5

def solution1(food_times, k):
    # []만 해도 힙큐 만들기 가능
    q = []

    # 최소힙 만들었음
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    taken_time = 0
    previous = 0
    length = len(food_times)
    # 이제 음식 시간 작은 순서대로 정렬됨
    while taken_time + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        taken_time += (now - previous) * length
        previous = now
        length -= 1
    
    result = sorted(q, key = lambda x: x[1])
    print(result)

    return result[(k - taken_time) % length][1]

    

print(solution1(food_times, k))

# 막힌 것들
    # 1. 최소힙 만드는 법
    # 2. while 조건
    # 3. sorted 사용법 및 인자에 람다 사용법
    # 4. 다 못 먹고 나왔을 때 남은 시간을 음식 개수로 나눈 나머지



def solution2(food_times, k):
    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    taken_times = 0
    previous_food_time = 0
    length = len(food_times)
    
    while taken_times + (q[0][0] - previous_food_time) * length <= k:
        now = heapq.heappop(q)[0]
        taken_times += (now - previous_food_time) * length
        previous_food_time = now
        length -= 1
    
    result = sorted(q, key = lambda x: x[1])

    return result[(k - taken_times) % length][1]