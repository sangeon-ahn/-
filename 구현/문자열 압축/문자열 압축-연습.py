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