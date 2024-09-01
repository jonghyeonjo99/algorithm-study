from itertools import combinations

def solution(clothes):
    answer = 1
    dic = dict()

    for cloth, Type in clothes:
        if(dic.get(Type) == None ):
            dic[Type] = [cloth]
            continue
        dic[Type].append(cloth)    

    for Type in dic:
        answer *= len(dic[Type]) + 1

    return answer - 1