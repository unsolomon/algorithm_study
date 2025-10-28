def solution(food):
    left = ''
    
    for i in range(1,len(food)):
        left += str(i) * (food[i] // 2)
    
    right = left[::-1]
    
    
    return left + '0' + right



# 0번쨰 배열은 항상 1 그리고 짝수개를 양옆으로 추가하는 방식으로 즉 <- 0 -> 식으로 늘어나느 형식
# 또한 늘어날때 들어가는 숫자는 배열 위치에 따른 값이 들어감

#조건 1. 중앙값은 항상 0
#조건 2. 배열 1번의 값이 홀수일때 -1 을 통해 1일때는 제외 짝수개만큼 양옆에 추가
#조건 3. 배열에 추가 되는 숫자는 배열의 위치값이 추가된 후 return