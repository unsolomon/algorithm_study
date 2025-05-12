def solution(n):
    j = []
    for i in range(1,n+1):
        if n % i == 0:
            j.append(i)   
    
    
    return j