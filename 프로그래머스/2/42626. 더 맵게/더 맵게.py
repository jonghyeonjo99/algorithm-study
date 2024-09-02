import heapq

def make_new_k(scoville):
    
    k1 = heapq.heappop(scoville)
    k2 = heapq.heappop(scoville)
    new_k = k1 + (k2*2)
    heapq.heappush(scoville, new_k)
    
    return scoville

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        else:
            make_new_k(scoville)
            answer += 1
    if scoville[0] < K:
        answer = -1
        
    return answer