import heapq
def solution(k, score):
    answer = []
    ha = []
    
    for i in score:
        heapq.heappush(ha,i)
        if len(ha) > k :
            heapq.heappop(ha)
            
        answer.append(ha[0])
        
    
    
    
    return answer

