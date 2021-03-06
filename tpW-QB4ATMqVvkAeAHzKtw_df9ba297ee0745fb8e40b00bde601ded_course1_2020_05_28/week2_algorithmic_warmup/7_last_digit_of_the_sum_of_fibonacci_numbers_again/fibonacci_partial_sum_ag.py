# Uses python3
import sys

def fibonacci_sum_fast(n):

    n = n % 60  # pisano period 0f 10 is 60

    previous = 0
    current  = 1
    sum      = 1

    if n<1:
        return 0

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum += current

    return sum % 10

def fibonacci_partial_sum_fast(from_, to):


    return (fibonacci_sum_fast(to) - fibonacci_sum_fast(from_ -1) +10) %10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))