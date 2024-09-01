def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        slicing_list = []
        for l in range(i-1, j):
            slicing_list.append(array[l])
        slicing_list.sort()
        answer.append(slicing_list[k-1])
    return answer