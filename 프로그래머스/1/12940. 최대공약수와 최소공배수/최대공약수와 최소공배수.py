def solution(n, m):
    answer = []
    answer1 = []
    
    #약수

    for i in range(1, n*m+1):
        if n % i == 0 and m % i == 0:
            answer1.append(i)
        
    # 배수
    for i in range(1, n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
                   
    
    return [max(answer1), min(answer)]