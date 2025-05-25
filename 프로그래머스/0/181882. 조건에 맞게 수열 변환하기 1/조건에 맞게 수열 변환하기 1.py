def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:    # 50 이상의 짝수는 2로 나눈다
            answer.append(i // 2)
        elif i < 50 and i % 2 == 1:   # 50 미만의 홀수는 2를 곱한다
            answer.append(i * 2)
        else:                          # 해당하지 않는 경우는 그대로
            answer.append(i)
    return answer
