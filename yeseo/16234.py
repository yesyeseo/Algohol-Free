import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

from collections import deque


N, L, R = map(int, input().split())
pplation = []
for _ in range(N): pplation.append(list(map(int, input().split())))

visit = [[0 for _ in range(N)] for _ in range(N)] # 이미 지나간 곳인지를 판별하는 리스트
ans = 0 # 몇 번 이동했는지를 판별함
move = [[+1, 0], [-1, 0], [0, +1], [0, -1]] # 인접 국경의 목록
union = [] # 연합 국가의 목록

# 국경선 오픈 여부를 판별하는 함수
def open(x, y):
    if L <= abs(pplation[x[0]][x[1]] - pplation[y[0]][y[1]]) <= R: return True
    return False

# 연합을 판별
def bfs(start):
    global visit
    this_union = [pplation[start[0]][start[1]], [start[0], start[1]]]
    # 현재 연합 리스트를 만들어 줌
    # 첫 번째 인덱스는 계산의 효율을 위해 연합군들의 합계로 함
    que = deque([start])
    visit[start[0]][start[1]] = 1
    while que:
        curr = que.popleft()
        for m in move:
            curr_m = [m[0] + curr[0], m[1] + curr[1]]
            if 0 <= curr_m[0] < N and 0 <= curr_m[1] < N and visit[curr_m[0]][curr_m[1]] == 0:
                # 국경 내부여야 하며 이미 방문한 곳이 아니여야 함
                if open(curr, curr_m):
                    # 국경이 열렸을 경우에만 방문 처리를 해 줌 - 해당 국경이 아래와는 연합일 확률 존재하기 때문
                    this_union.append(curr_m)
                    this_union[0] += pplation[curr_m[0]][curr_m[1]]
                    # 현재 연합의 인구수의 총 수는 반복문을 돌릴 때 함께 계산하여 줌
                    if visit[curr_m[0]][curr_m[1]] == 0: que.append(curr_m)
                    visit[curr_m[0]][curr_m[1]] = 1
    return this_union

def move_once():
    global ans, visit, union
    # 한번 이동했을 때 pplation 계산
    for i in range(N):
        for j in range(N):
            if sum(sum(v) for v in visit) == N*N: break
            if visit[i][j] == 1: continue
            union_start = bfs([i, j])
            if len(union_start) > 2: union.append(union_start)

    # print(union)
    if len(union) == 0:
        print(ans)
        return
    # 만약 인구 이동이 발생하지 않는다면 바로 몇 번 이동하였는지 출력함
    # 인구 이동이 발생하지 않았음을 더 빨리 알아챌 수 있는 방법이 있을까?
    else:
        ans += 1
        # 연합을 이루는 각 칸의 인구수를 계산함
        # 계산의 편의를 위하여 union 만드는 과정에서 각 그룹의 첫 인수는 총 인구수로 미리 계산
        for u in union:
            if len(u) == 2: continue
            pplation_mod = int(u[0] / (len(u) - 1))
            for i in u[1:]:
                pplation[i[0]][i[1]] = pplation_mod

        visit = [[0 for _ in range(N)] for _ in range(N)]
        union = []
        move_once()
        # 다시 인구 이동을 시작

move_once()