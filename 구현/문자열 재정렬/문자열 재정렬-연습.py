import string


def solution():
    data = input()
    result = []
    sum = 0;

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            sum += int(x)
    
    result.sort()

    if sum != 0:
        result.append(str(sum))

    return ''.join(result)

print(solution())

# 생각 못한 것들
    # 1. 받은 문자열에 숫자가 없을 때를 예외처리하기 위해 if sum != 0 해줘야 한다.


