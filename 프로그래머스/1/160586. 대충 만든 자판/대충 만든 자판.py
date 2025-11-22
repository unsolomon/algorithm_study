def solution(keymap, targets):

    min_presses = {}
    for idx, keys in enumerate(keymap):
        for i, ch in enumerate(keys):

            presses = i + 1
            if ch in min_presses:
                min_presses[ch] = min(min_presses[ch], presses)
            else:
                min_presses[ch] = presses

    result = []
    for word in targets:
        total = 0
        for ch in word:
            if ch in min_presses:
                total += min_presses[ch]
            else:
                total = -1
                break
        result.append(total)
    return result
