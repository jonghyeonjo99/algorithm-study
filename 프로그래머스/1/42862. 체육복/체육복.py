def solution(n, lost, reserve):
    answer = 0
    students = [1 for _ in range(n)]
    for i in lost:
        students[i-1] -= 1
    for i in reserve:
        students[i-1] += 1
        
    for i in range(len(students)):
        if students[i] == 0:
            if 0 <= i-1 < n and students[i-1] == 2:
                students[i-1] = 1
                students[i] = 1
                continue
            elif 0 <= i+1 < n and students[i+1] == 2:
                students[i+1] = 1
                students[i] = 1
                continue
        
    for i in students:
        if i >= 1:
            answer += 1
    return answer