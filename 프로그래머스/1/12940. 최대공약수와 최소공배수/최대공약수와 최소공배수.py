def gcd(n,m):
    if n % m == 0:
        return m
    else:
        return gcd(m,n%m)
def solution(n,m):
    return [gcd(m,n), n*m//gcd(m,n)]