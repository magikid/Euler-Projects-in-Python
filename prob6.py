#!/usr/bin/env python

def prob6(low, high):

	a = range(low,high)
	for item in a[:]:
		a[item] = pow(item,2)
		print a[item]
	a = sum(a[:])
	print "a = " + str(a)

	b = pow(sum(range(low,high)), 2)
	print "b = " + str(b)

	print "b - a = " + str(b-a)
	
prob6(0,101)
