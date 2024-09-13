from collections import Counter

def solution(points, routes):
    answer = 0
    routes_log = [[] for _ in range(len(routes))]
    
    for i in range(len(routes)):
        route = routes[i]
        routes_log[i].append(points[route[0] - 1])
        for j in range(len(route)-1):
            # routes_log[i].append(points[route[j] - 1])
            temp_x = points[route[j] - 1][0]
            temp_y = points[route[j] - 1][1]
            # 현재 위치에서 다음 위치 비교 x먼저
            if points[route[j] - 1][0] > points[route[j+1] - 1][0]:
                temp_x = points[route[j] - 1][0]
                while temp_x > points[route[j+1] - 1][0]:
                    temp_x -= 1
                    routes_log[i].append([temp_x, temp_y])
            elif points[route[j] - 1][0] < points[route[j+1] - 1][0]:
                temp_x = points[route[j] - 1][0]
                while temp_x < points[route[j+1] - 1][0]:
                    temp_x += 1
                    routes_log[i].append([temp_x, temp_y])
            # y 움직임
            if points[route[j] - 1][1] > points[route[j+1] - 1][1]:
                temp_y = points[route[j] - 1][1]
                while temp_y > points[route[j+1] - 1][1]:
                    temp_y -= 1
                    routes_log[i].append([temp_x, temp_y])
            elif points[route[j] - 1][1] < points[route[j+1] - 1][1]:
                temp_y = points[route[j] - 1][1]
                while temp_y < points[route[j+1] - 1][1]:
                    temp_y += 1
                    routes_log[i].append([temp_x, temp_y])
    # print(routes_log)
    count = 0
    for i in range(len(routes_log)):
        count = max(count, len(routes_log[i]))
    
    for i in range(count):
        result = []
        for j in range(len(routes_log)):
            if i < len(routes_log[j]): 
                result.append(routes_log[j][i])
        
        # 리스트를 튜플로 변환하여 중복을 찾기 위해 Counter 사용
        result_counter = Counter(tuple(r) for r in result)
        
        # 중복된 좌표가 있는 경우, 그 개수만큼 answer 증가
        for key, count in result_counter.items():
            if count > 1:
                answer += 1  # 중복된 좌표의 개수만큼 추가
        
    return answer