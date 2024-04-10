import sys
from itertools import permutations

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
cal_list = list(map(int,sys.stdin.readline().split()))

comb_list = []
# 덧셈
for i in range(cal_list[0]):
    comb_list.append(0)
#뺄셈
for i in range(cal_list[1]):
    comb_list.append(1)
#곱셈
for i in range(cal_list[2]):
    comb_list.append(2)
#나눗셈
for i in range(cal_list[3]):
    comb_list.append(3)

cal_comb_list = set(permutations(comb_list,len(comb_list)))

result_list = []
#사칙연산 함수
def cal_rule(num_list,cal_comb):
    result = init_cal(num_list,cal_comb) # 맨 처음 계산 하고 난 결과값
    for i in range(1,len(num_list)-1):
        if(cal_comb[i] == 0):
            result += num_list[i+1]
        elif(cal_comb[i] == 1):
            result -= num_list[i+1]
        elif(cal_comb[i] == 2):
            result *= num_list[i+1]
        elif(cal_comb[i] == 3):
            if(result < 0):
                result = -(-result // num_list[i+1])
            else:
                result //= num_list[i+1]
    result_list.append(result)

def init_cal(num_list,cal_comb):
    result = 0
    if(cal_comb[0] == 0):
        result = num_list[0] + num_list[1]
    elif(cal_comb[0] == 1):
        result = num_list[0] - num_list[1]
    elif(cal_comb[0] == 2):
        result = num_list[0] * num_list[1]
    elif(cal_comb[0] == 3):
        result = num_list[0] // num_list[1]
    return result

for cal_comb in cal_comb_list:
    cal_rule(num_list,cal_comb)

result_list.sort()

print(result_list[-1])
print(result_list[0])


