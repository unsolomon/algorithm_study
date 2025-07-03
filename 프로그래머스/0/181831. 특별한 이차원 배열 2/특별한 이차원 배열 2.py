def solution(arr):
    answer = len(arr)
    
    for i in range(answer):
        for j in range(answer):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
    
    
    return answer