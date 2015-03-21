#!/usr/bin/env python
# _*_ coding: utf8 _*_

import logged, sys

class Tmp(object):
    '''doc'''
    def __init__(self):
        self.power = 5
    def set_power(self, power):
        self.power = power
    def met(self, val):
        return val**self.power

@logged.log(sys.stdout)
def print_val(t):
    print t.power
    print t.met(10)

t = Tmp()

print_val(t)
t.set_power(6)
print_val(t)
