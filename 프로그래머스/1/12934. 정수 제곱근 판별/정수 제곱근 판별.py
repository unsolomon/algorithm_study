def solution(n):
    x = n ** 0.5                 # n의 제곱근
    if x == int(x):              # 제곱근이 정수라면 (즉, x가 양의 정수)
        return int(x+1) ** 2     # (x+1)의 제곱
    else:
        return -1
