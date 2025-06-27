def solution(arr, k):
    if k % 2 == 1:  # k가 홀수일 때
        return [i * k for i in arr]
    else:           # k가 짝수일 때
        return [i + k for i in arr]
