def solution(s):
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = s
    for i,word in enumerate(words):
        
        answer = answer.replace(word,str(i))
    
    
    
    
    return int(answer)