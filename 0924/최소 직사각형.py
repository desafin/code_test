def solution(sizes):
    # 두 가지 리스트를 초기화합니다. 하나는 폭(width), 다른 하나는 높이(height)를 저장하기 위한 것입니다.
    width = []
    height = []
    answer = 0  # 최종적으로 반환할 결과를 저장할 변수를 초기화합니다.

    # sizes 리스트의 각 원소에 대해 반복합니다.
    for i in range(len(sizes)):
        # 현재 크기(i번째 크기)에서 최대값을 폭 리스트에 추가합니다.
        width.append(max(sizes[i]))
        # 현재 크기(i번째 크기)에서 최소값을 높이 리스트에 추가합니다.
        height.append(min(sizes[i]))

    # 모든 크기에서 최대 폭과 최소 높이를 계산한 후,
    # 최대 폭과 최소 높이를 곱한 값을 최종 결과 변수(answer)에 할당합니다.
    answer = max(width) * max(height)

    # 최종 결과를 반환합니다.
    return answer
sol=[[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sol))