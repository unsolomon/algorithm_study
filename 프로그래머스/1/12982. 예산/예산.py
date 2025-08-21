def solution(d, budget):
    answer = 0
    count = 0 
    d.sort()
    
    for i in d:
        answer += i
        if answer <= budget:
            count += 1
        else:
            break
            
    return count




# s사에서 각 부서당 구매물풀 조사
#예산한저ㅏㅇ
#각 부서 최소 금액지원
# 각 주서별 지원 금 d
#예산 budge
# 최대 몇개의 부서에 물품 지원
