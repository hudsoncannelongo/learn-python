def fib(n: int):
    """
    Prints Fibonacci numbers up to n

    Args
     n (int): Max number
    """

    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
