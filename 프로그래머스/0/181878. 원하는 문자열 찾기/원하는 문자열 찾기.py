def solution(myString, pat):
    
    my = myString.lower()
    pa = pat.lower()
    
    if pa in my:
        return 1
    else :
        return 0
    
