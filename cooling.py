
t_str = raw_input("Enter the current temperature of the tea!:")
t = int(t_str)

a_str = raw_input("Enter the current temperature of the air!:")
a = int(a_str)

m_str = raw_input("Enter the number of minutes that have passed!:")
m = int(m_str)

print '{} {}'.format('minutes', 'temperature')


i = 0
while i < m:

    t = t - ((t - a) * .055)
    i += 1
    print '{}       {}'.format(i , t)
#Its kind of a table haha

"""
File: cooling.py

Copyright (c) 2016 Lucas Blair

License: MIT

This code computes the final temperature of any temperature of tea after any amount of minutes placed in a room of any temperature. Kinda confusing but still really cool.

"""    
