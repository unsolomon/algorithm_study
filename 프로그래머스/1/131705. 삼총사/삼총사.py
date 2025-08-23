from itertools import combinations

def solution(number):
    answer = 0
    
    for cum in combinations(number,3):
        
        if sum(cum) == 0:
            answer +=1
    
    
    
    
    
    return answer


