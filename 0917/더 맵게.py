import heapq

#https://school.programmers.co.kr/learn/courses/30/lessons/42626
def solution(scoville, K):
    # 최소 힙으로 변환

    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K and len(scoville) > 1:
        # 힙에서 두 개의 최소 요소를 추출하여 더하고 다시 힙에 넣음
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)
        cnt = cnt + 1
    if scoville[0] < K:
        return -1
    return cnt



