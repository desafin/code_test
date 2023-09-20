def compare(x, y):
    # x와 y를 두 가지 방법으로 합쳐서 비교합니다.
    # 더 큰 숫자가 앞에 오도록 정렬합니다.
    if x + y > y + x:
        return 1
    elif x + y < y + x:
        return -1
    else:
        return 0

def solution(numbers):
    # 숫자를 문자열로 변환합니다.
    numbers = list(map(str, numbers))

    # 정렬 함수를 사용하여 숫자를 정렬합니다.
    numbers.sort(key=functools.cmp_to_key(compare), reverse=True)

    # 모든 숫자가 0인 경우를 처리하기 위해 int로 변환 후 다시 문자열로 변환합니다.
    answer = str(int(''.join(numbers)))

    return answer

# 필요한 모듈을 임포트합니다.
import functools

# 테스트 입력
numbers = [10, 2, 3, 9]

# 함수 호출
result = solution(numbers)

print("가장 큰 숫자:", result)
