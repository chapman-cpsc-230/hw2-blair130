import math

b_str = input ("Enter a base number:")
b = float(b_str)


n_str = input ("Enter a natural number:")
n = int(n_str)

i = 0
sum = 0


while i <= n:
    sum += pow (b, i)
    i += 1

print "The result is %d" %sum

print "The second part of the problem is %d" %(pow (b, ((n+1)/(b-1))))

"""
File: sum_powers.py

Copyright (c) 2016 Lucas Blair

License: MIT

This code finds the value of b^n and the value of b^((n+1)/(b-1))

"""    
