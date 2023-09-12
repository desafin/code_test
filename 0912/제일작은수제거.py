#https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    if len(arr) <= 1:
        return [-1]

    min_value = min(arr)  # 배열에서 최솟값 찾기
    arr.remove(min_value)  # 최솟값 제거

    return arr
