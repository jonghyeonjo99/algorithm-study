import sys
from itertools import combinations
INF = int(1e9)

n,m = map(int, sys.stdin.readline().rstrip().split())

city = []
for i in range(n):
  city_input = list(map(int,sys.stdin.readline().rstrip().split()))
  city.append(city_input)

chicken =[]
houses = []
for i in range(n):
  for j in range(n):
    if(city[i][j] == 2):
      chicken.append((i,j))
    elif(city[i][j] == 1):
      houses.append((i,j))

select_chicken = list(combinations(chicken,m))

answer = []

def chicken_distance(chickenList):

  result = 0
  for i,j in houses:
    distance = INF
    for x, y in chickenList:
      distance = min(distance, (abs(i-x) + abs(j-y)))
    result += distance
  return result

for chicken_list in select_chicken:
  dis = chicken_distance(chicken_list)
  answer.append(dis)

print(min(answer))
    

