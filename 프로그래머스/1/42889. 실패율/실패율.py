def solution(N, stages):
    answer = []
    total_players = len(stages)
    stage_fail_rate = []
    
    for stage in range(1, N + 1):

        reached = sum(1 for s in stages if s >= stage)

        not_cleared = stages.count(stage)
        fail_rate = not_cleared / reached if reached else 0
        stage_fail_rate.append((stage, fail_rate))

    stage_fail_rate.sort(key=lambda x: (-x[1], x[0]))
    answer = [stage for stage, rate in stage_fail_rate]
    return answer