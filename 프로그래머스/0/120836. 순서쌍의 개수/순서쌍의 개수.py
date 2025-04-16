def solution(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):  # 1부터 √n까지 탐색
        if n % i == 0:
            if i == n // i:  # i가 √n인 경우 (예: n=4, i=2)
                count += 1
            else:            # i와 n/i가 다른 경우
                count += 2
    return count
