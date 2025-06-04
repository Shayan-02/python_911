def memorize(func):
    mamad = {}

    def wrapper(*args):
        if args in mamad:
            return mamad[args]
        result = func(*args)
        mamad[args] = result
        return result

    return wrapper


@memorize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(440))
