from collections import deque

def solution(priorities,location):
    # 큐 초기화
    queue = deque()
    answer=0
    # 프로퍼티스 값과 인덱스를 튜플로 묶어 큐에 추가
    for index, prop in enumerate(priorities):
        queue.append((prop, index))

    # 큐 확인 (테스트를 위해 출력)
    print(queue)

    location=location-1

    while queue:
        current_element = queue.popleft()  # 큐에서 요소를 하나 뽑음
        current_priority, current_index = current_element  # 요소의 프로퍼티 값과 인덱스를 가져옴

        is_max = all(current_priority >= prop for prop, _ in queue)  # 현재 요소가 큐의 다른 요소들보다 우선순위가 높은지 확인

        if not is_max:
            queue.append(current_element)  # 현재 요소가 최댓값보다 작으면 큐 맨 뒤로 다시 넣음
        else:
            print(str(current_element)+"제거")
            answer=answer+1
            if current_index == location:
                print(current_element)
                print(answer)
                return answer


# 예시 호출
solution([1, 1, 9, 1, 1, 1],3)