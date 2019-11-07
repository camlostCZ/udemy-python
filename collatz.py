def collatz_conjecture(n, steps=0):
    print("#{}: {}".format(steps, n))
    if n == 1:
        result = steps
    elif n < 1:
        raise ValueError("Parameter 'n' has to be > 1.")
    else:
        if n % 2 == 0:
            result = collatz_conjecture(int(n // 2), steps + 1)
        else:
            result = collatz_conjecture(3 * n + 1, steps + 1)
    return result

x = collatz_conjecture(25)
