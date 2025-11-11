def solution(k, m, score):
    score.sort(reverse=True)
    n = len(score)//m
    answer = 0
    
    for i in range(n):
        answer += score[(i+1) * m-1] * m
        
    
    return answer