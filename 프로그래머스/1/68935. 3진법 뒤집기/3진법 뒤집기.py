def solution(n):
    answer = []
    while n > 0:
        answer.append(str(n%3))
        n //= 3
        
    re_st = "".join(answer)
    
    
    answer = int(re_st,3)
    
    
    
    return answer