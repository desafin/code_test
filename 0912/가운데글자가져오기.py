#https://school.programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    answer = ''

    intlen = len(s)

    if intlen % 2 != 0:
        answer = s[intlen // 2]
    else:
        answer = s[intlen // 2 - 1:intlen // 2 + 1]
    return answer