import sys
import functools


def takes(*parameters):
    def actual_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for arg, type_arg in zip(args, parameters):
                if not isinstance(arg, type_arg):
                    raise TypeError
            return function(*args, **kwargs)
        return wrapper
    return actual_decorator


exec(sys.stdin.read())
