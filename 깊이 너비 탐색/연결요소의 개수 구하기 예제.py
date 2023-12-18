import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(10000)

# DFS 정의
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# 예제 입력 대신 사용할 입력 데이터
example_input = [
    "6 5\n",
    "1 2\n",
    "2 5\n",
    "5 1\n",
    "3 4\n",
    "4 6\n"
]

# 입력 처리 함수
def input():
    return example_input.pop(0)

# 입력 받기
n, m = map(int, input().split())

# 그래프 초기화
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

# 연결 요소 개수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

# 결과 출력
print(count)
