def solution(arr):
    answer = []
    
    for i in range(0,len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i]  != arr[i-1]:
            answer.append(arr[i])

    return answer