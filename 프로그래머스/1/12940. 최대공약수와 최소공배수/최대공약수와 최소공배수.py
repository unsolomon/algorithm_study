import math
def solution(n, m):
    gcd = math.gcd(n,m)
    answer  = n*m//gcd
    
    
    return [gcd,answer]