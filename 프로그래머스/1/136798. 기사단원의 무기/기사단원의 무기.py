def solution(number, limit, power):
    def count_d(n):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n%i ==0:
                cnt +=2 if i != n// i else 1
        return cnt
    
    total_weight = 0 
    for i in range(1, number+1):
        div_count = count_d(i)
        if div_count > limit:
            total_weight += power
        else:
            total_weight += div_count 
    
    return total_weight