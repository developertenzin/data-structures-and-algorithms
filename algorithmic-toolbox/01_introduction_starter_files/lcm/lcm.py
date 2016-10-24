# Uses python3
import sys
"""
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
"""
def gcd_fast(a, b):
    if b == 0:
        return a
    return gcd_fast(b, a%b)

def lcm_fast(a, b):
    """
    >>> lcm_fast(28851538, 1183019)
    1933053046

    >>> lcm_fast(226553150, 1023473145)
    46374212988031350
    """
    gcd = gcd_fast(a, b)
    return (a*b)//gcd

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

