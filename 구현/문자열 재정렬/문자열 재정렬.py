# 숫자와 문자를 구별하는 법이 궁금하다

def solution():
    data = input()
    result = []
    value = 0

    # 문자를 하나씩 확인하며
    for x in data:
        # 알파벳인 경우 결과 리스트에 삽입
        if x.isalpha():
            result.append(x)
        # 숫자는 따로 더하기
        else:
            value += int(x)
    
    # 알파벳을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))
    
    # 최종결과 출력(리스트를 문자열로 변환하여 출력)
    print(''.join(result))

solution()

# 알게된 점
    # 1. 문자열의 특정 인덱스가 알파벳인지 확인하는 법
        # x.isalpha()
    # 2. 리스트를 문자열로 변환하는 법
        # ''.join(result) (result리스트의 요소 사이에 ''를 삽입해서 문자열로 만듬. 지금은 ''라서 바로 붙여버림)
