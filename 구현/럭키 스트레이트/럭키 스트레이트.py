n = input()
length = len(n)
summary = 0


# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")

# 알게된 점
    # 1. 인풋으로 받은 숫자는 인덱스 접근이 가능하다.
    # 2. // 연산자는 몫을 구할 때 사용한다.