def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    
    def find(x):
        
        if parent[x] == x:
            return x
        
        return find(parent[x])
    
    def union(x,y):
        x = find(x)
        y = find(y)
        
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
            
    for cost in costs:
        a, b, pay = cost
        if find(a) != find(b):
            union(a,b)
            answer += pay
    
    
    return answer