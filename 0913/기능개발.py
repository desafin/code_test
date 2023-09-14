#각 작업의 배포일 계산하기:
#주어진 작업의 진도와 속도를 이용하여 각 작업이 언제 배포될 수 있는지 계산합니다. 진도가 100%가 될 때까지 작업이 완료되어야 하므로, 남#은 작업량을 계산하여 속도로 나눈 후 올림 처리를 하여 배포일을 계산합니다.
#배포일에 따라 작업 수 세기:

#계산된 배포일을 이용하여 각 배포일마다 몇 개의 작업이 배포될 수 있는지 세어봅니다. 첫 번째 배포일부터 순서대로 작업의 개수를 세면 됩니다.
#결과 반환:

#작업 수를 센 결과를 배열에 저장하여 반환합니다.

import math

def solution(progresses, speeds):
    remain_progress = []
    for element in range(len(progresses)):
        temp = math.ceil((100 - progresses[element]) / speeds[element])
        remain_progress.append(temp)

    result = []
    i = 0

    while i < len(remain_progress):
        current_element = remain_progress[i]
        count = 0

        while i < len(remain_progress) and remain_progress[i] <= current_element:
            count += 1
            i += 1

        result.append(count)

    return result