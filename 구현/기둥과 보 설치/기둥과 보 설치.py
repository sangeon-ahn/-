# possible 함수
# solution 함수

# answer 배열 만들고
# frame 받아서 for 돌리면서
# 기둥이나 보 answer배열에 넣고 이 answer배열을 possible 함수에 넣어서 가능한지 파악
# 가능하면 넘어가고 안되면 answer 에서 remove로 넣었던거 없애기
# for 끝나면 answer 리턴



def isPossible(answer):
    for [x, y, a] in answer:
   
        if a == 0 and (y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer):
            print(1)
            continue

        if a == 1 and ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
            print(2)
            continue
        print(3)
        return False
    return True


def solution(n, build_frame):
    answer = []

    for [x, y, a, b] in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if isPossible(answer):
                continue
            else:
                answer.remove([x, y, a])
        else:
            if [x, y, a] in answer:
                answer.remove([x, y, a])
                if isPossible(answer):
                    continue
                else:
                    answer.append([x, y, a])
            else:
                continue
    
    return sorted(answer)
        

n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(n, build_frame))

# 이번에는 코드를 보고 치는게 아니라 답 코드를 먼저 이해한 후, 내가 이해한걸 바탕으로 적어보았다.
# 보고 치는건 효율적이지 못하다고 생각해서 이렇게 해보았다.
# 이 문제의 핵심은 보, 기둥이 존재할 수 있는 조건을 어떻게 구현할지인데, 여기서는 배열을 이용해서 이걸 구현했다.
# 그리고 answer 배열 내에 들어가 있는 모든 구조물의 가능성 여부를 각각 따진다.