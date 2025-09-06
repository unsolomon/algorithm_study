def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        
        a = bin(arr1[i] | arr2[i])[2:].zfill(n)
        line = a.replace('1','#').replace('0',' ')
    
        answer.append(line)
    
    return answer