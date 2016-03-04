
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
