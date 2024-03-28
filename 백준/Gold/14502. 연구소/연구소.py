import sys
from collections import deque
from itertools import combinations
import copy

n, m = map(int,sys.stdin.readline().rstrip().split())

labs = []
for i in range(n):
    lab = list(map(int,sys.stdin.readline().rstrip().split()))
    labs.append(lab)

virus = []
empty = []
for i in range(n):
    for j in range(m):
        if(labs[i][j] == 2):
            virus.append((i,j))
        elif(labs[i][j] == 0):
            empty.append((i,j))

combs = list(combinations(empty,3))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(gragh,x,y):
    queue = deque()
    queue.append((x,y))

    while(queue):
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < n and 0 <= ny < m):
                if(gragh[nx][ny] == 0):
                    gragh[nx][ny] = 2
                    queue.append((nx,ny))

result = []
for comb in combs:
    count = 0
    labs_copy = copy.deepcopy(labs)

    for i,j in comb:
        labs_copy[i][j] = 1
    
    for x,y in virus:
        bfs(labs_copy,x,y)

    for a in range(n):
        for b in range(m):
            if(labs_copy[a][b] == 0):
                count += 1
        
    result.append(count)

print(max(result))