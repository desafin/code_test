from itertools import permutations


def solution(numbers):
    # 모든 가능한 순열 생성
    all_permutations = list(permutations(numbers))

    # 각 순열을 문자열로 변환한 후 정수로 변환하여 리스트에 저장
    permutation_integers = [int(''.join(map(str, perm))) for perm in all_permutations]

    # 정수 리스트를 내림차순으로 정렬
    permutation_integers.sort(reverse=True)

    # 가장 큰 숫자를 문자열로 변환하여 반환
    max_number = str(permutation_integers[0])

    return max_number

# 테스트 입력
numbers = [10, 2, 3, 9]

# 함수 호출
result = solution(numbers)

print("가장 큰 숫자:", result)