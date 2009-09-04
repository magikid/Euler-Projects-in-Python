#!/usr/bin/env python

def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True

x = 0
b = list()
for a in range(2,1000000):
	if isprime(a):
		b.append(a)

print "10001st prime = " + str(b[10000])

