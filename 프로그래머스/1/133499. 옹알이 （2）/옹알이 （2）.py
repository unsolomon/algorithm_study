def solution(babbling):
    answer = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        if any(p*2 in word for p in answer):
            continue
        temp = word
        for p in answer:
            temp = temp.replace(p, ' ')
        if temp.strip() == '':
            count += 1
    return count
