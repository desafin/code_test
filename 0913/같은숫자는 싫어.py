def solution(arr):
    # 큐 생성
    answer = []

    temp = None

    for item in arr:
        if answer is None or temp != item:  # temp가없으면 빈 큐
            answer.append(item)  # 배열에 요소 추가
            temp = item

    return answer