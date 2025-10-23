def solution(sizes):
    wi = []
    he = []
    
    for w,h in sizes:
        wi.append(max(w,h))
        he.append(min(w,h))
    
    
    return max(wi) * max(he)