def prime_number(number):
    num = int(number) ** 0.5
    for i in range(2,int(num)+1):
        if int(number) % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    result = []
    while n >= k:
        temp = n % k
        n = n // k
        result.append(str(temp))
    result.append(str(n))
    
    sort_result = []
    for i in range(len(result)):
        latter = result.pop()
        sort_result.append(latter)
        
    total_number = ''.join(sort_result)

    total_number = total_number.split('0')
    # print(total_number)
    for number in total_number:
        if number != '1' and number != '':
            if prime_number(number):
                answer += 1
        
    
    return answer