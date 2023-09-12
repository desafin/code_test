#https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0

    length = len(nums)

    num = length / 2  # 뽑을수있는 수

    # 중복제거

    unique_list = list(set(nums))

    unique_list_len = len(unique_list)  # 종류의 갯수

    if num > unique_list_len:
        return unique_list_len
    else:
        return num