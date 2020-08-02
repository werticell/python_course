import sys
import functools
from time import time


def profiler(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if not wrapper.isCalled:
            wrapper.rec_depth = 0
            wrapper.calls = 0
            wrapper.last_time_taken = -time()
            wrapper.isCalled = True

        wrapper.rec_depth += 1
        wrapper.calls += 1
        result = function(*args, **kwargs)
        wrapper.rec_depth -= 1

        if wrapper.rec_depth == 0:
            wrapper.last_time_taken += time()
            wrapper.isCalled = False

        return result

    wrapper.isCalled = False
    return wrapper


exec(sys.stdin.read())
