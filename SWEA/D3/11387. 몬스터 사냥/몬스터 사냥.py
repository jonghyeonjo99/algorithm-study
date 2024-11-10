t = int(input())
for i in range(t):
    d, l, n = map(int, input().split())

    total_attack = 0
    for j in range(n):
        total_attack += d * (1 + j * l * 0.01)

    print("#%d %d" % (i+1,int(total_attack)))