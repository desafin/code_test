def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):#첫번쨰 요소뺴고 다음요소에서 반복문 끝날떄까지 반복
            if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
                answer = False
                break  # 일치하는 경우가 발견되면 반복문 종료
        if not answer:
            break

    return answer


solution(["119", "97674223", "1195524421"])