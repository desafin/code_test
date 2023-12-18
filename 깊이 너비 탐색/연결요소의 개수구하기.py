import sys

# 재귀 호출의 최대 깊이를 늘려주는 설정입니다.
# DFS를 사용할 때, 호출 깊이가 깊어질 수 있기 때문에 필요합니다.
sys.setrecursionlimit(10000)

# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# 정점의 수 n과 간선의 수 m을 입력받습니다.
n, m = map(int, input().split())

# 각 노드에 연결된 노드를 저장할 리스트 A를 생성합니다.
# n+1의 크기로 생성하는 이유는 노드 번호가 1부터 시작하기 때문입니다.
A = [[] for _ in range(n + 1)]

# 노드의 방문 여부를 체크할 리스트입니다.
# 처음에는 모든 노드를 '방문하지 않음' 상태(False)로 설정합니다.
visited = [False] * (n + 1)

# DFS 함수 정의
# v: 현재 방문하고 있는 노드
def DFS(v):
    # 현재 노드를 방문한 것으로 표시합니다.
    visited[v] = True
    # 현재 노드와 연결된 모든 노드에 대해
    for i in A[v]:
        # 아직 방문하지 않은 노드가 있다면 DFS를 재귀적으로 호출합니다.
        if not visited[i]:
            DFS(i)

# 간선 정보 입력
# m번 반복하여 간선 정보를 입력받습니다.
for _ in range(m):
    s, e = map(int, input().split())
    # 무방향 그래프이므로, 노드 s에 e를 추가하고, 노드 e에 s를 추가합니다.
    A[s].append(e)
    A[e].append(s)

# 연결 요소의 수를 세는 변수입니다.
count = 0

# 모든 노드를 순회합니다.
for i in range(1, n + 1):
    # 아직 방문하지 않은 노드를 찾으면
    if not visited[i]:
        # 연결 요소의 수를 하나 증가시키고
        count += 1
        # 해당 노드에서 DFS를 시작합니다.
        DFS(i)

# 연결 요소의 총 수를 출력합니다.
print(count)
