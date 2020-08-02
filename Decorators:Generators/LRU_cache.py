import functools


def cache(size_of_cache):

    def actual_wrapper(function):
        memory = {}
        recently_used = []

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            tmp = str(args) + str(kwargs)
            if tmp not in memory:
                if len(recently_used) >= size_of_cache:
                    memory.pop(recently_used.pop(0))
                memory[tmp] = function(*args, **kwargs)
                recently_used.append(tmp)
            else:
                recently_used.remove(tmp)
                recently_used.append(tmp)
            return memory[tmp]
        return wrapper

    return actual_wrapper
