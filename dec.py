import functools

def d(func):
    @functools.wraps(func)
    def c(*dt, **mp):
        print "called {}({} {})".format(func.__name__, dt, mp)
        return func(*dt, **mp)
    return c
@d
def f(x):
    return x+1
print f(1)
