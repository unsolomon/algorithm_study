def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    numbers.sort()
    
    for i in numbers:
        answer.remove(i)
        
    
    
    return sum(answer)