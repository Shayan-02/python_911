import time


def t(f):
    def w(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print(f"{end_time - start_time:.10f} seconds")
        return result
    return w


@t
def slow_function():
    s = 0
    for i in range(200_000_000):
        s += i
    print(s)


slow_function()
