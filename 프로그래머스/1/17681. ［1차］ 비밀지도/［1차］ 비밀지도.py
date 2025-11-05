def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        
        b_s = bin(arr1[i] | arr2[i])[2:].zfill(n)
        line = ''
        for c in b_s:
            if c == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    
    
    
    return answer