def solution(num_list):
    answer = len(num_list)
    
    if answer >= 11:
        a= 0
        for i in num_list:
            a += i
        return a
    else:
        a = 1
        for i in num_list:
            a *= i
        return a
            
    
    
    
