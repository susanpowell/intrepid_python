from sys import argv

script, first, second, third, last = argv

guess = raw_input('What do you think the first variable is? '),

print "You thought the first variable would be %s." % guess

"""For some reason it is not seeing,
 guess == first, even when they are the same"""
 
if guess == first:
	print ("You were right!")
else:
	print ("Sorry, you were wrong.")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "You last variable is:", last