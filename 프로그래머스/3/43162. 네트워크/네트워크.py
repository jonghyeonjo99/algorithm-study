def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    
    def find(a):
        if parent[a] == a:
            return a
        return find(parent[a])
    
    def union(a,b):
        p_a = find(a)
        p_b = find(b)
    
        if p_a < p_b:
            parent[p_b] = p_a
        else:
            parent[p_a] = p_b
    
    for i in range(n):
        for j in range(i):
            if computers[i][j] == 1:
                union(j,i)
    
    # print(parent)
    
    # parent_set = set(parent)
    # answer = len(parent_set)
    parent_set = set()
    for i in range(n):
        parent_set.add(find(parent[i]))
    answer = len(parent_set)
    
    return answer