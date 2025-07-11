def solution(arr, n):
    answer = []
    length = len(arr)
    for i in range(length):
        # 홀수 길이: 짝수 인덱스에 n 더하기
        if length % 2 == 1 and i % 2 == 0:
            answer.append(arr[i] + n)
        # 짝수 길이: 홀수 인덱스에 n 더하기
        elif length % 2 == 0 and i % 2 == 1:
            answer.append(arr[i] + n)
        else:
            answer.append(arr[i])
    return answer
