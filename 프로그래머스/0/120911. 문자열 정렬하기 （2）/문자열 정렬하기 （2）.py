def solution(my_string):
    answer = []
    my_string = my_string.lower()
    
    answer = list(my_string)
    answer.sort()
    return (''.join(answer))