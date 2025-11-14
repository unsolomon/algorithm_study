def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    count = 0
    for word in babbling:
        temp = word
        for c in can:
            if c*2 in temp:
                break  
        else:
            for c in can:
                temp = temp.replace(c, ' ')
            if temp.strip() == '':
                count += 1
    return count
