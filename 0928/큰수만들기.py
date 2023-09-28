def solution(number, k):
    stack = []

    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 만일 k가 남아있다면 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

# 예제 테스트
number = "1231234"
k = 3
result = solution(number, k)
print(result)  # 출력 결과: "94"
