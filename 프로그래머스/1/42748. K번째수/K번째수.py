def solution(array, commands):
    answer = []
    for i,k,j in commands:
        sliced   = array[i-1:k]
        sliced.sort()
        answer.append(sliced[j-1])
    
    
    
    return answer