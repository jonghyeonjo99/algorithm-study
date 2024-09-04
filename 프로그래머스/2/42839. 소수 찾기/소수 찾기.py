from itertools import permutations


def solution(numbers):
    answer = 0
    number_list = list(numbers)
    # print(number_list)
    
    result = []
    for i in range(1,len(number_list) + 1):
        all_number_list = list(permutations(number_list, i))
        for j in range(len(all_number_list)):
            result.append(int(''.join(all_number_list[j])))
    
    result = list(set(result))
    print(result)

    for i in range(len(result)):
        flag = False
        for j in range(2, int(result[i] ** 0.5) + 1):
            if result[i] % j == 0:
                flag = True
                break
        if flag == False and result[i] != 0 and result[i] != 1:
            answer += 1
        
            
        
        
    
    return answer