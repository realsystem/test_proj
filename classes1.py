class A(object):
    def __init__(self):
        print "A.init"
    def d(self, pt):
        print "A.d"
    def cl(self):
        print "A.cl"

class B(A):
    def __init__(self):
        print "B.init"
    def d(self, pt):
        print "B.d"
#        A.d(self, pt)
        super(B, self).d(pt)

class C(A):
    def __init__(self):
        print "C.init"
    def d(self, pt):
        print "C.d"
#        A.d(self, pt)
        super(C, self).d(pt)
    def cl(self):
        print "C.cl"

class D(B, C):
    def __init__(self):
        print "D.init"
    def d(self, pt):
        print "D.d"
#        B.d(self, pt)
#        C.d(self, pt)
        super(D, self).d(pt)

d=D()
d.d(1)
