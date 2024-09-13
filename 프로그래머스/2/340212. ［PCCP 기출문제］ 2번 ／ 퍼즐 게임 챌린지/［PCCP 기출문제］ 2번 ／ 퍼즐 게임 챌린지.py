def solution(diffs, times, limit):
    answer = float('inf')
    
    start = 1
    end = 100000
    while start <= end:
        # mid 값은 유저의 숙련도
        mid = (start + end) // 2
        temp = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                temp += times[i]
            else:
                temp += ((diffs[i] - mid) * (times[i-1] + times[i])) + times[i]
        # print(temp)
        
        if temp <= limit:
            end = mid - 1
            if mid <= answer:
                answer = mid
        else:
            start = mid + 1
        
    return answer