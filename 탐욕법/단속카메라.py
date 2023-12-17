def solution(routes):
    # 경로를 종료 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    camera_count = 0
    camera_position = -30001  # 카메라 위치 초기화 (문제의 제한 조건에서 가능한 최소값보다 작게 설정)

    for route in routes:
        # 현재 카메라 위치가 해당 차량의 경로를 포함하지 않으면
        if camera_position < route[0]:
            # 카메라를 해당 차량의 경로 종료 지점에 설치
            camera_position = route[1]
            camera_count += 1

    return camera_count
