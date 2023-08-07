import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

union = []

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    union=[(r, c)]
    
    visited[r][c]=1
    people = A[r][c]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and L<=abs(A[nx][ny]-A[x][y])<=R:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                people+=A[nx][ny]
                union.append((nx, ny))
    
    if len(union)>1:
        for i, j in union:
            A[i][j] = people//len(union)
        return 1
    return 0
    
days = 0

while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag = max(flag, bfs(i, j))
    if flag == 0:
        break
    days+=1

print(days)