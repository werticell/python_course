from heapq import merge


def merge_sorter(*args):
    iterator = merge(*args)
    flag = True
    while flag:
        try:
            item = next(iterator)
            yield item
        except StopIteration:
            flag = False
            pass
