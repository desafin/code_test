def solution(sizes):
    answer = 0
    pocket = 0
    wMax = 0
    hMax = 0

    for i in range(len(sizes)):  # 1. len(sizes) 대신 range(len(sizes)) 사용
        if sizes[i][0] < sizes[i][1]:
            pocket = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = pocket

        if wMax < sizes[i][0]:
            wMax = sizes[i][0]

        if hMax < sizes[i][1]:
            hMax = sizes[i][1]

    answer = wMax * hMax  # 중복된 answer 할당 제거
    return answer

a=solution([[60, 50], [30, 70], [60, 30], [80, 40]])
print(a)