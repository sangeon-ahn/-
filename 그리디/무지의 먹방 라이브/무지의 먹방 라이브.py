import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬, 이유는 위에서는 우선순위 큐로 정렬을 했기 때문에 음식 시간 기준으로 정렬이 되어있다.
    print(result)
    return result[(k - sum_value) % length][1]

food_times = [8, 6, 4]
k = 15

a = solution(food_times, k)

print(a)

# 알게된 점
    # 1. 힙푸시 할때 최소힙으로 만드는데 최소의 기준은 두번째 인자로 하고 만약 set 구조가 들어왔다면 set 인자의 첫번째 값을 기준으로 만든다.
    # 2. q는 그자체로 힙이 될 수 있다.
    # 3. 힙팝을 하면 가장 작은 값이 나오고 다시 힙구조로 만든다.
    # 4. sorted 에서 key = lambda x: x[1]같이 어떻게 람다함수 작성하는지 배움
    