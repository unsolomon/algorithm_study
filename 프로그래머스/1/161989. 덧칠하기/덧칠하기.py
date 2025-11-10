def solution(n, m, section):
    answer = 0
    
    i = 0
    length = len(section)
    
    while i < length:
        roll_end = section[i] + m -1
        answer += 1
        
        
        while i < length and section[i] <= roll_end:
            i += 1
    
    
    return answer