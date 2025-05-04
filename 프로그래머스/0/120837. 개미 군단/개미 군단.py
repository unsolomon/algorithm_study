def solution(hp):
    generals = hp // 5          # 장군개미 수[1]
    remainder = hp % 5          # 장군개미 사용 후 남은 체력[1]
    soldiers = remainder // 3   # 병정개미 수[1]
    workers = remainder % 3     # 일개미 수[1]
    return generals + soldiers + workers
