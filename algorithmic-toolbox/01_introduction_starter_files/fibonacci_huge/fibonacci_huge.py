# Uses python3
import sys
def find_pisano_period(mod_num):
    """
    Finds the pisano period pattern of the fibonacci series getting divided by the mod_num.
    :param mod_num:
    :return: int
    """
    previous, current = 0, 1
    count = 0
    while True:
        count += 1
        previous, current = current, previous + current
        if previous % mod_num == 0 and current % mod_num == 1:
            return count

def get_fibonacci_huge_naive(n, m):
    """
    Returns the Fib(n) % m by leveraging the pisano period.
    :param n:
    :param m:
    :return: int
    """
    previous, current = 0, 1
    pisano_period = find_pisano_period(m)
    remainder = n % pisano_period
    for _ in range(remainder):
        previous, current = current, previous + current
    return previous % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))






