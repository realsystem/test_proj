#!/usr/bin/env python
# _*_ coding: utf8 _*

import sys

def log(fd):
	def c1(func):
		def c2(*args, **kwargs):
			print "called %s" % func.__name__
			res=func(*args, **kwargs)
			print "end of call %s" % func.__name__
			return res
		return c2
	return c1

@log(sys.stdout)
def r(x,y):
	print x

r(1,2)
