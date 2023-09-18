#https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 접근방식 모든 배열의 요소를 1자리수의 숫자로 바꾸자
# ex 13= 1과 3
# 그다음에 내림차순 정렬하면 해결

def solution(numbers):
    digits = []
    # 각 자리수를 분리하여 리스트에 저장
    for numbers in numbers:
        number = numbers[numbers]

        while number > 0:
            digit = number % 10
            digits.append(digit)
            number //= 10

    # 리스트를 역순으로 출력하면 각 자리의 값을 얻을 수 있습니다.
    reversed_digits = digits[::-1]

    print(reversed_digits)

solution([6, 10, 2])