import sys
from itertools import combinations
import heapq

n = int(sys.stdin.readline().rstrip())
people = []
for i in range(n):
    people.append(i)


board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

team_list = list(combinations(people, n//2))

num = len(team_list)//2

#축구 팀 만듬
team_set = []
for i in range(num):
    team_set.append((team_list[i],team_list[len(team_list)-1-i]))

#각각의 축구 팀 능력치 계산 함수
def team_power(team):
    power = 0
    team_pair = list(combinations(team,2))
    for x,y in team_pair:
        power += board[x][y] + board[y][x]
    return power

#두 축구팀의 능력치 비교값 저장
def sub_team_power(team1_power, team2_power):
    sub_power = abs(team1_power - team2_power)
    return sub_power

result = []
for team1, team2 in team_set:
    team1_power = team_power(team1)
    team2_power = team_power(team2)
    sub_power = sub_team_power(team1_power,team2_power)
    heapq.heappush(result,sub_power)

min_sub = heapq.heappop(result)

print(min_sub)
