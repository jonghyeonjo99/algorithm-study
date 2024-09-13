from itertools import product

def solution(users, emoticons):
    answer = []
    users = sorted(users, key = lambda x : (-x[0], -x[1]))
    emoticons = sorted(emoticons, key = lambda x : -x)

    for sale_rate in product([40,30,20,10], repeat = len(emoticons)):
        temp_answer = [0,0]
        for rate, total_cost in users:
            temp_total = 0
            for i in range(len(emoticons)):
                # 이모티콘 할인율이 유저 할인율보다 높거나 같으면
                if sale_rate[i] >= rate:
                    temp_total += emoticons[i] * (1 - (sale_rate[i] * 0.01))
            # 이모티콘 판매액이 유저 기준 금액보다 높거나 같으면
            if temp_total >= total_cost:
                temp_answer[0] += 1
            else:
                temp_answer[1] += temp_total
            answer.append(temp_answer)
    answer = sorted(answer, key = lambda x : (-x[0], -x[1]))
    answer = answer[0]
    
    return answer