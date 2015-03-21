class A(object):
    def __init__(self, x):
        self.x = 12
class B(A):
    def __init__(self, x, y):
        A.__init__(self, y)
        self.y = y
    def ssum(self):
        return self.x+self.y

b=B(1,2)
print b.ssum()
