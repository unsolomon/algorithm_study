def solution(a, b):
    answer = int(str(a)+str(b))
    answer1 = int(str(b)+str(a))
    
    if answer > answer1:
        return answer
    else:
        return answer1
    