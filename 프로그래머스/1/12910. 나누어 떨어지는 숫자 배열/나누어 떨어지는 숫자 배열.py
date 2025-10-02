def solution(arr, divisor):
    j = []
    for i in arr:
        if i%divisor == 0 :
            j.append(i)
    if not j :
        return [-1]
    
    return sorted(j)