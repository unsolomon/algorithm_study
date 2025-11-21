def solution(lottos, win_nums):
    matched = len(set(lottos) & set(win_nums))
    zero_count = lottos.count(0)    
    best = matched + zero_count

    def get_rank(n):
        if n >= 6:
            return 1
        elif n == 5:
            return 2
        elif n == 4:
            return 3
        elif n == 3:
            return 4
        elif n == 2:
            return 5
        else:
            return 6
    
    return [get_rank(best), get_rank(matched)]
