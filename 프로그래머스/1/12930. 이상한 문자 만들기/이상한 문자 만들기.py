def solution(s):
    answer = ''
    index = 0
    
    for char in s:
        if char == ' ':
            index = 0
            answer += ' '
            
        else:
            if index % 2 == 0:
                answer += char.upper()
                
            else:
                answer += char.lower()
                
            index += 1
            
    return answer
    
    