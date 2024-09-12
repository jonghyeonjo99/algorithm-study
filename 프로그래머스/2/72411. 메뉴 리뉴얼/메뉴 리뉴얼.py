from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        temp = []
        for order in orders:
            if len(order) >= i:
                order_list = list(combinations(sorted(order),i))
                for j in order_list:
                    str = ''.join(j)
                    temp.append(str)
        temp.sort()
        counter = Counter(temp)
        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for latter, count in counter.items():
                    if count == max_count:
                        answer.append(latter)
    answer.sort()
    return answer