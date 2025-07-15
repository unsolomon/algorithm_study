def solution(myString):
    answer = []
    an = []
    
    for i in myString:
        if i == 'x':
            an.append(len(answer))
            answer = []
        else:
            answer.append(i)
        
    
    an.append(len(answer))
    return an