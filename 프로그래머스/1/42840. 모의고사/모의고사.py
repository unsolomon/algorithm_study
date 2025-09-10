def solution(answers):
    so1 = [1,2,3,4,5]
    so2 = [2,1,2,3,2,4,2,5]
    so3 = [3,3,1,1,2,2,4,4,5,5]

    count1, count2, count3 = 0, 0, 0

    for idx, ans in enumerate(answers):
        if ans == so1[idx % len(so1)]:
            count1 += 1
        if ans == so2[idx % len(so2)]:
            count2 += 1
        if ans == so3[idx % len(so3)]:
            count3 += 1

    max_score = max(count1, count2, count3)
    result = []
    if count1 == max_score:
        result.append(1)
    if count2 == max_score:
        result.append(2)
    if count3 == max_score:
        result.append(3)

    return result
