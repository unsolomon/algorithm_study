def solution(X, Y):
    # 각 숫자(0~9)가 X, Y에서 몇 번씩 나오는지 카운트
    cntX = [0] * 10
    cntY = [0] * 10
    for ch in X:
        cntX[int(ch)] += 1
    for ch in Y:
        cntY[int(ch)] += 1

    answer = []

    # 9부터 0까지 공통으로 존재하는 개수만큼 붙이기
    for d in range(9, -1, -1):
        common = min(cntX[d], cntY[d])  # 짝지을 수 있는 개수
        if common > 0:
            answer.append(str(d) * common)

    if not answer:
        return "-1"

    result = "".join(answer)

    # 짝꿍이 0으로만 구성된 경우
    if result[0] == "0":   # 가장 큰 자리도 0이면 전부 0뿐
        return "0"

    return result
