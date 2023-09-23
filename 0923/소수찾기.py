from itertools import permutations


def solution(numbers):
    number_str = str(numbers)


    #permutations_list = list(permutations(number_list))

    # 문자열을 한 글자씩 쪼개서 리스트에 추가
    number_list = [char for char in number_str]

    # 순열을 저장할 리스트를 초기화합니다.
    permutations_list = []

    time=len(number_list)

    # 모든 가능한 순열을 생성합니다.
    for i in range(time):
        permutations_list.extend(list(map(''.join, permutations(number_list, i+1))))

    #순열을 정수로 변환하여 저장할 리스트
    integer_permutations = []



    #순열을 정수로 변환하고 저장

    for permutation in permutations_list:
        int_permutation = int(''.join(map(str, permutation)))
        integer_permutations.append(int_permutation)

    # 중복된 요소 제거
    unique_list = list(set(permutations_list))

    # unique_list의 각 요소를 정수로 변환하여 새로운 리스트 생성
    integer_unique_list = [int(item) for item in unique_list]

    # 결과
    result = []



    # 소수인가
    for item in integer_unique_list:
       if item <= 1:
           result.append(item)
           continue

       elif item == 2:

           result.append(item)
           continue

       elif item % 2 == 0:
           result.append(item)
           continue

       for i in range(3, int(item ** 0.5) + 1, 2):
            if item % i == 0:
                result.append(item)

    for item in result:
        integer_unique_list.remove(item)

    print(integer_unique_list)
    print(result)
    return len(integer_unique_list)


print(solution(11))