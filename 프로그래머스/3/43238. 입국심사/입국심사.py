def solution(n, times):
    answer = (n+1) * max(times)
    
    start = 0
    end = (n+1) * max(times)
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(len(times)):
            count += mid // times[i]
    
        if count < n:
            start = mid + 1
        elif count >= n:
            end = mid - 1
            answer = min(mid, answer)
            
    return answer