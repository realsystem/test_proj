#!/usr/bin/env python
# _*_ coding: utf8 _*
_
def check_prime(n):
	for x in xrange(2,n):
		if n%x == 0:
			break
	else:
		yield n

def gen_primes():
	n=2
	while True:
		 check_prime(n)
		n+=1

it=gen_primes()
for p in it:
	print p
