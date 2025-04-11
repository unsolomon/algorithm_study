def solution(sides):
    # 배열을 정렬하여 가장 긴 변을 찾음
    sides.sort()
    # 삼각형 조건: 가장 긴 변 < 나머지 두 변의 합
    if sides[2] < sides[0] + sides[1]:
        return 1  # 삼각형을 만들 수 있음
    else:
        return 2  # 삼각형을 만들 수 없음
