def solution(s):
    count = 0
    while s:
        x = s[0]
        x_count = 0
        other_count = 0
        for i, ch in enumerate(s):
            if ch == x:
                x_count += 1
            else:
                other_count += 1
            if x_count == other_count:
                count += 1
                s = s[i+1:]
                break
        else:
           
            count += 1
            break
    return count
