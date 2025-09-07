def solution(number, limit, power):
    def count_divisors(n):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                cnt += 1
                if i != n // i:
                    cnt += 1
        return cnt

    total = 0
    for knight in range(1, number+1):
        attack = count_divisors(knight)
        if attack > limit:
            attack = power
        total += attack

    return total
