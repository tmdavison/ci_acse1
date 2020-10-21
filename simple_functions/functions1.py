
__all__ = ['my_sum']


def my_sum(iterable):
    ''' sums iterable '''
    tot = 0
    for i in iterable:
        tot += i
    return tot
