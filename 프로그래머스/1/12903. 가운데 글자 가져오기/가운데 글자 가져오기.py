def solution(s):
    answer = len(s)
    
    if answer%2 == 0:
        return s[answer//2-1:answer//2+1]
    else:
        return s[answer//2]
    
    