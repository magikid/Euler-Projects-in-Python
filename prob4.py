#!/usr/bin/env python

biggestnum = 0
a = 1
b = 1
c = a * b

for a in range(1,999):
	for b in range(1,999):
		c = a * b
		if (str(c) == str(c)[::-1]) == True:
			if c > biggestnum:
				biggestnum = c
		b = b - 1
	a = a - 1
print biggestnum
