def solution(participant, completion):
    answer = ''
    flag = False
    sort_participant = sorted(participant)
    sort_completion = sorted(completion)
    
    for i in range(len(sort_completion)):
        if sort_completion[i] != sort_participant[i]:
            answer = sort_participant[i]
            flag = True
            break
    
    if flag == False:
        answer = sort_participant[-1]
    return answer