def solution(t, p):
    count = 0
    len_p = len(p)
    p = int(p)  # 숫자로 변환
    
    for i in range(len(t) - len_p + 1):
        sub = int(t[i:i+len_p])  # 부분 문자열 잘라서 정수 변환
        if sub <= p:
            count += 1
            
    return count
