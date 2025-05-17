def solution(a, b):
    answer = 0
    
    c = str(a)+str(b)
    c = int(c)
    d = 2*a*b
    
    if c > d:
        return c
    else:
        return d
    