def solution(num_list):
    answer = 0
    
    a = len(num_list)
    b,c = 0,0
    for i in range(0,a):
        if (i+1) % 2 == 1:
            b += num_list[i]
        else:
            c += num_list[i]
            
    if b > c:
        return b
    else :
        return c
    