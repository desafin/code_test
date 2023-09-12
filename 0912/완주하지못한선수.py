#https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant_dict = {}  # 참가자를 저장할 딕셔너리 생성

    # 참가자 목록을 딕셔너리에 추가하고 개수를 카운트
    for person in participant:
        if person in participant_dict:
            participant_dict[person] += 1#중복이라면 1명씩 추가
        else:
            participant_dict[person] = 1# 1명새로 생성

    # 완주자 목록을 딕셔너리에서 차감
    for person in completion:
        participant_dict[person] -= 1#1명씩 빼기

    # 딕셔너리에서 값이 1인 참가자를 찾아 반환
    #미 완주자
    for person, count in participant_dict.items():
        if count == 1:
            return person


