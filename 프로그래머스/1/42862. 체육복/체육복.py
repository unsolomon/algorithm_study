def solution(n, lost, reserve):
    # 여벌 체육복이 있는데 도난당한 학생 처리: 여분과 도난에서 모두 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    # 빌려줄 수 있는 경우 처리
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    
    # 전체 학생 수에서 남은 lost 명을 뺀다
    return n - len(lost_set)
