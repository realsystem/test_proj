import sys
import functools

def d(stream):
    def c1(func):
        @functools.wraps(func)
        def c2(*dt, **mp):
            stream.write("called {}({} {})".format(func.__name__, dt, mp))
            return func(*dt, **mp)
        return c2
    return c1
@d(sys.stderr)
def f(x):
    return x+1
print f(1)
