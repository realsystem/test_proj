#!/usr/bin/env python
# _*_ coding: utf8 _*
_
class X(object):
	def t(self):
		return self
x=X()
print x.t()
print X.t(x)
print X.t()
