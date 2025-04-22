def solution(dot):
    x,y =  dot[0], dot[1]
    if x  >= 1:

        if y  >=1:
            return 1
        else : 
            return 4
    elif x  <= 1:

        if y   >=1:
            return 2
        else : 
            return 3

    
    return answer