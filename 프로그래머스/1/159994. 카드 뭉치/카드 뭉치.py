def solution(cards1, cards2, goal):
    i, j = 0, 0  # 각 카드 뭉치의 인덱스
    
    
    for k in goal:
        
        if  i < len(cards1) and k == cards1[i]:
            i += 1
        elif j < len(cards2) and k == cards2[j]:
            j += 1
        else:
            return 'No'
    
    return "Yes"