def solution(wallet, bill):
    res = []
    for i in range(2):
        b = bill[:]    # 얕은 복사(파괴 방지)
        w = wallet[:]  # 얕은 복사(회전 방지)
        if i == 1:     # 90도 회전
            b[0], b[1] = b[1], b[0]
        cnt = 0
        while b[0] > w[0] or b[1] > w[1]:
            if b[0] >= b[1]:
                b[0] //= 2
            else:
                b[1] //= 2
            cnt += 1
            # 만약 한 변이 이미 1 이하라면 더이상 접어봤자 의미 없음
            if b[0] == 0 or b[1] == 0:
                break
        if b[0] <= w[0] and b[1] <= w[1]:
            res.append(cnt)
    return min(res) if res else -1
