def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1


    return answer
# 예시 입력
numbers1 = [1, 1, 1, 1, 1]
target1 = 3
numbers2 = [4, 1, 2, 1]
target2 = 4

# 예시 출력
print(solution(numbers1, target1))  # 출력: 5
print(solution(numbers2, target2))  # 출력: 2
