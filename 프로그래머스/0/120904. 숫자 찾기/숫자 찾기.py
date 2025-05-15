def solution(num, k):
    answer = str(num)
    
    a = 0
    
    for i in answer:
        a += 1
        if k == int(i):
            return a
    return -1
