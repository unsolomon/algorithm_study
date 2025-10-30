def solution(array, commands):
    answer = []
    a= 0
    for i,j,k in commands:
        q = sorted(array[i-1:j])
        answer.append(q[k-1])
        
    
    
    return answer


