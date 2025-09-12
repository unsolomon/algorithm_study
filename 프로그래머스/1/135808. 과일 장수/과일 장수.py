def solution(k, m, score):
    # 점수 내림차순 정렬
    score.sort(reverse=True)
    profit = 0
    
    # m개씩 묶어서 상자 만들기
    for i in range(0, len(score) - m + 1, m):
        box = score[i:i+m]
        profit += min(box) * m   # 상자의 최저 점수 × m
    
    return profit
