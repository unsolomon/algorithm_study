def solution(s):
    answer = len(s)
    mid = answer //2

    if answer %2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]