#!/usr/bin/env python
#I'm the best there ever was!

n = 600851475143

def prime_factors(n):  
    """ Return the prime factors of the given number. """  
    factors = []  
    lastresult = n  
  
    # 1 is a special case  
    if n == 1:  
        return [1]  
  
    while 1:  
        if lastresult == 1:  
            break  
  
        c = 2  
  
        while 1:  
            if lastresult % c == 0:
            	print "lastresult % c == 0, c= " + str(c)
                break  
  
            c += 1  
  
        factors.append(c)  
        lastresult /= c
  
    return factors  

print prime_factors(n)
