def solution(s):
    answer = []
    last_positions = {}  
    
    for i,ch in enumerate(s):
        if ch not in last_positions:
            answer.append(-1)
        else:
            answer.append(i -last_positions[ch] )
        
        last_positions[ch] = i  # 현재 위치로 업데이트
    
    
    
    return answer




# 1.문자열 s의 각 s의 각 위치보다 앞에 나왔으며 가장 가까운 곳에 있는 같은 글자




