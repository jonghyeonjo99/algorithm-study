import heapq

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # for i in range(len(numbers)):
    #     numbers[i] = str(numbers[i]) + '000'
    numbers.sort(key = lambda x: x*3, reverse = True)
    # print(numbers)
    # for i in numbers:
    #     answer += i[:-3]
    # answer = str(int(answer))
    answer = str(int(''.join(numbers)))
    return answer