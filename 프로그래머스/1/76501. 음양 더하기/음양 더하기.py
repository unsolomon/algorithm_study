def solution(absolutes, signs):
    answer = 0
    
    
    for i,x in zip(absolutes,signs):
        if x:
            answer += i
        else:
            answer -= i
            
    
    
    return answer