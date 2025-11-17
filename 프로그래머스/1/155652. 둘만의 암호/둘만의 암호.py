def solution(s, skip, index):
    answer = ''
    
    skip_set = set(skip)
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)if chr(i) not in skip_set]
    
    
    for ch in s:
        pos = alphabet.index(ch)
        new_pos = (pos + index)% len(alphabet)
        answer += alphabet[new_pos]
    
    
    
    return answer