import numpy as np


def solution(answers):
    answer = []
    first_array = [1, 2, 3, 4, 5] * ((len(answers) // 5) + 1)
    second_array = [2, 1, 2, 3, 2, 4, 2, 5] * ((len(answers) // 8) + 1)
    third_array = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((len(answers) // 10) + 1)

    first_cnt = 0
    second_cnt = 0
    third_cnt = 0

    for i in range(len(answers)):
        if answers[i] == first_array[i]:
            first_cnt = first_cnt + 1
        if answers[i] == second_array[i]:
            second_cnt = second_cnt + 1
        if answers[i] == third_array[i]:
            third_cnt = third_cnt + 1

    answer = []
    if first_cnt >= second_cnt and first_cnt >= third_cnt:
        answer.append(1)
    if second_cnt >= first_cnt and second_cnt >= third_cnt:
        answer.append(2)
    if third_cnt >= first_cnt and third_cnt >= second_cnt:
        answer.append(3)

    return answer