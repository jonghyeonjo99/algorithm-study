def solution(genres, plays):
    answer = []
    dic = dict()
    for i in range(len(genres)):
        if dic.get(genres[i]):
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
    
    dic_key = list(dic)
    dic_value = list(dic.values())
    
    list_dic = []
    for i in range(len(dic_key)):
        list_dic.append((dic_key[i], dic_value[i]))
    list_dic.sort(key = lambda x : -x[1])
    
    play_list = []
    for i in range(len(genres)):
        play_list.append([i,genres[i], plays[i]])
    play_list.sort(key = lambda x : (x[1], -x[2], x[0]))
    
    result = [[] for _ in range(len(list_dic))]
    for j in range(len(list_dic)): 
        for i in range(len(play_list)):
            if play_list[i][1] == list_dic[j][0]:
                result[j].append(play_list[i][0])
    # print(result)
    
    for res in result:
        if len(res) == 1:
            answer.append(res[0])
        else:
            answer.append(res[0])
            answer.append(res[1])
                
    return answer