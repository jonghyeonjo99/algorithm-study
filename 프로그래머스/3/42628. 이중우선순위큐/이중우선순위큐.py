import heapq

def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    count = 0
    for i in operations:
        oper = i.split(' ')
        if oper[0] == 'I':
            #힙 구조에 append
            heapq.heappush(min_heap, int(oper[1]))
            heapq.heappush(max_heap, -int(oper[1]))
            count += 1
        elif oper[0] == 'D' and count > 0:
            if oper[1] == '-1':
                # 최소힙 구조에서 최솟값 삭제
                count -= 1
                poped = heapq.heappop(min_heap)
                max_heap.remove(-poped)
            elif oper[1] == '1':
                # 최대힙 구조에서 최댓값 삭제
                count -= 1
                poped = heapq.heappop(max_heap)
                min_heap.remove(-poped)
        
    if not min_heap:
        return [0,0]
    
    answer.append(-heapq.heappop(max_heap))
    answer.append(heapq.heappop(min_heap))
    
    return answer