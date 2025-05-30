def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1 and i >= idx:
            return i
    return -1
