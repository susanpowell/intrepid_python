from sys import argv

script, filename = argv

print "We're going to read the file we just made."

test = open(filename)

print test.read()

test.close()