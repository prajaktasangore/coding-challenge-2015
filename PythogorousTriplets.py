#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Prajakta Sangore
# Date:   30th September 2015
# Problem: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#			a2 + b2 = c2
#			For example, 32 + 42 = 9 + 16 = 25 = 52.
#			There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#			Find the product abc.


import time
import decimal

start_time = time.time()

def pythagorous():

	for  a in xrange (1,1000):
		for b in xrange(2,1000):
			c = 1000 - (a+b)
			if((a**2) + (b**2) == (c**2)):
				if(a + b + c == 1000):
					print "a = %d b =%d c = %d" %(a,b,c)
					print "The sum is = %d" %(a+b+c)
					print "The product is = %d" %(a*b*c)
					return 1

pythagorous()
print "total time taken = %s seconds" %round((time.time() - start_time),2)
