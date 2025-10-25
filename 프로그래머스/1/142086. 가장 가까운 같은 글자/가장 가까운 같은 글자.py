def solution(s):
    answer = []
    idex = {}
    for i,ch in enumerate(s):
        if ch in idex:
            answer.append(i-idex[ch])
        else:
            answer.append(-1)
            
        idex[ch] = i
        
        
    return answer
            