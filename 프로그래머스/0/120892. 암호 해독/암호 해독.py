def solution(cipher, code):
    # code의 배수 번째(1-based) 문자만 추출
    return ''.join(cipher[i] for i in range(code-1, len(cipher), code))
