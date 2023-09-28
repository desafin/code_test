def solution(people, limit):
    people.sort()  # 무게를 오름차순으로 정렬

    cnt = 0  # 보트의 수를 세는 변수
    left = 0  # 가장 가벼운 사람의 인덱스
    right = len(people) - 1  # 가장 무거운 사람의 인덱스

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람과 가장 무거운 사람을 함께 태움
        right -= 1  # 가장 무거운 사람은 항상 보트에 탑승

        cnt += 1  # 보트 개수 증가

    return cnt

print(solution([70,50, 80, 50],100))