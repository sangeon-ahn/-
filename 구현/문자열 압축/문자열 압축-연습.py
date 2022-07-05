def solution1(s):
    answer = s
    for step in range(1, len(s) // 2 + 1):
        prev = s[0:step]
        compressed = ''
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j + step]
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
        
        if len(answer) > len(compressed):
            answer = compressed
    
    return answer

print(solution1('abcabcabcabcd'))

# 어려웠던 점들
    # 1. prev와 현재 스텝 단위문자열이 같지 않을 때 새로운 prev와 카운트 초기화를 해줘야 하는데 이걸 깜빡했다.
    # 2. 각 스텝별 내부 for문이 끝났을 때 남은 문자열이 있다는 걸 생각하기 어려웠다. prev와 같은 경우 count += 1 된채로 for문을 빠져나올 것이고, 
    #   같지 않을 경우에는 prev에 마지막 스텝에 해당하는 문자열 조각이 들어있다.
    