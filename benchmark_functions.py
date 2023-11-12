from functools import lru_cache

def fibonacci(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n, memo={}):
    if n in (0,1):
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        
    return memo[n]

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)