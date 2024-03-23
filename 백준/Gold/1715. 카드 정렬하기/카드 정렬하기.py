import sys
import heapq

n = int(sys.stdin.readline().rstrip())

cardList = []
for i in range(n):
    card = int(sys.stdin.readline().rstrip())
    heapq.heappush(cardList, card)

count = 0
while(len(cardList) > 1):
    low_card1 = heapq.heappop(cardList)
    low_card2 = heapq.heappop(cardList)
    sum_card = low_card1 + low_card2
    count += sum_card
    heapq.heappush(cardList,sum_card)

print(count)