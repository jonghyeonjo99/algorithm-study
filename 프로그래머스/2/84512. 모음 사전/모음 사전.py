from itertools import permutations

def solution(word):
    answer = 0
    words = ["A","A","A","A","A","E","E","E","E","E","I","I","I","I","I","O","O","O","O","O","U","U","U","U","U"]
    words_list_1 = list(set(permutations(words,1)))
    words_list_2 = list(set(permutations(words,2)))
    words_list_3 = list(set(permutations(words,3)))
    words_list_4 = list(set(permutations(words,4)))
    words_list_5 = list(set(permutations(words,5)))
    words_list_1.extend(words_list_2)
    words_list_1.extend(words_list_3)
    words_list_1.extend(words_list_4)
    words_list_1.extend(words_list_5)
    
    words_list_1.sort()
    
    result = []
    for i in words_list_1:
        str = ''.join(i)
        result.append(str)
    
    
    answer = result.index(word) + 1
    
    return answer