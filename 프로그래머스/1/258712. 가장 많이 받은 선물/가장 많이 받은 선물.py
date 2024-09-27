from itertools import combinations

def solution(friends, gifts):
    answer = 0
    friends_idx = dict()
    people = []
    for i in range(len(friends)):
        people.append(i)

    for i in range(len(friends)):
        friends_idx[friends[i]] = i
    # print(friends_idx)
    
    board = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    # print(board)
    
    for gift in gifts:
        giver, receiver = gift.split(' ')
        board[friends_idx.get(giver)][friends_idx.get(receiver)] += 1
    
    gift_num = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        temp = 0
        for j in range(len(friends)):
            temp += board[i][j]
        for j in range(len(friends)):
            temp -= board[j][i]
        gift_num[i] = temp
    
    next_gift = [0 for _ in range(len(friends))]
    comb = combinations(people, 2)
    for g, r in comb:
        # 주고받은 기록이 있고, 서로 같지 않다면
        if (board[g][r] != 0 or board[r][g] != 0) and board[g][r] != board[r][g]:
            a = board[g][r]
            b = board[r][g]
            if a > b:
                next_gift[g] += 1
            else:
                next_gift[r] += 1
        # 주고 받은 기억이 없거나, 서로 같다면
        else:
            a_num = gift_num[g]
            b_num = gift_num[r]
            if a_num > b_num:
                next_gift[g] += 1
            elif a_num < b_num:
                next_gift[r] += 1
            else:
                continue
    
    answer = max(next_gift)
    
    return answer