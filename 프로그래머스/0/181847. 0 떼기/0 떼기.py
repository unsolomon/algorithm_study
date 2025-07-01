def solution(n_str):
    lst = list(n_str)
    while lst and lst[0] == '0':
        lst.pop(0)
    answer = ''.join(lst)
    return answer