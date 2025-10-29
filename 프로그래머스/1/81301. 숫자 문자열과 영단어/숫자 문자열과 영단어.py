def solution(s):
    answer = ['zero','one','two','three','four','five','six','seven','eight','nine']
    result = ''
    for i,z in enumerate(answer):
        s = s.replace(z,str(i))
    return int(s)

