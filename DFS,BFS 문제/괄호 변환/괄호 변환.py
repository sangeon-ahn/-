input = input()

def solution(str):
  answer = ''

  if not str:
    return ''

  [u, v] = splitString(str)

  if isCorrectString(u):
    answer = u + solution(v)
  else:
    answer = '('
    answer += solution(v)
    answer += ')'

    u = u[1:-1]
    reversed_u = ''

    for i in range(len(u)):
      if u[i] == '(':
        reversed_u += ')'
      else:
        reversed_u += '('
    
    answer += reversed_u
  
  return answer

def splitString(str):
  left_count = 0
  right_count = 0

  for i in range(len(str)):
    if str[i] == '(':
      left_count += 1
    elif str[i] == ')':
      right_count -= 1

    if left_count + right_count == 0:
      return [str[0 : i+1], str[i+1:]]

def isCorrectString(str):
  count = 0

  for i in range(len(str)):
    if str[i] == '(':
      count += 1
    else:
      count -= 1

    if count < 0:
      return False

  return count == 0

print(solution(input))

# 전에 풀어본 문제다
# 쉬운편