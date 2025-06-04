import time


def zamansanj(asghar):
    def dakheli(*args, **kwargs):
        start_time = time.time()
        result = asghar(*args, **kwargs)
        end_time = time.time()
        print(f"{asghar.__name__} ran in {end_time - start_time} seconds")
        return result

    return dakheli


@zamansanj
def slow_function():
    sums = 0
    for i in range(500_000_000):
        sums += i
    return sums


print(slow_function())
