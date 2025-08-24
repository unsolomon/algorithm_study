def solution(s):
    result = []
    idx = 0  # 단어 내 인덱스
    for ch in s:
        if ch == ' ':
            result.append(' ')
            idx = 0  # 단어 시작
        else:
            if idx % 2 == 0:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
            idx += 1
    return ''.join(result)
