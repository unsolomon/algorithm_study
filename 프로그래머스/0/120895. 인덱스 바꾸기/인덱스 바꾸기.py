def solution(my_string, num1, num2):
    answer = ''
    
    st = list(my_string)
    
    st[num1], st[num2] = st[num2],st[num1]
    
    
    return ''.join(st)