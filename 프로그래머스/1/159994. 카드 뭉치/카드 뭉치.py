def solution(cards1, cards2, goal):
    answer = ''
    idx , idx2 = 0,0
    n,n2 = len(cards1),len(cards2)
    
    for word in goal:
        if idx < n and cards1[idx] == word:
            idx += 1
        elif idx2 < n2 and cards2[idx2] == word:
            idx2 += 1
            
        else : 
            return "No"
    
    
    
    
    return "Yes"


