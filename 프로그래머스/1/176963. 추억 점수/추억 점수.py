def solution(name, yearning, photo):
    answer = []
    score_map = dict(zip(name,yearning))
    
    for g in photo:
        score = sum(score_map.get(person,0)for person in g)
        answer.append(score)
    
    return answer

