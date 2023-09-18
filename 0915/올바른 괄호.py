def solution(priorities, location):
    answer = 0

    my_dict = {}  # 빈 딕셔너리 생성

    # 반복문을 사용하여 키와 값을 딕셔너리에 추가
    for i in range(len(priorities)):
        my_dict[priorities[i]] = i[i]

    return my_dict

solution("ABCD")