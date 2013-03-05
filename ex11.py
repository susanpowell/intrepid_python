print "How old are you?",
age = int(raw_input())
print "How old is your mother?",
mom_age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input('Enter in pounds, please:')

birth_age = mom_age - age

print """
	So you're %r years old, your mother was %r when you were born,
	you're %r tall, and weigh %r pounds.
	""" % (age, birth_age, height, weight)