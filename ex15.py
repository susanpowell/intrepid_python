#import a module to use in this script
from sys import argv

#define the values required for the script to run
script, filename = argv

#txt is defined as the file object returned by doing the command "open"
txt = open(filename)

#prints a simple statement
print "Here's your file %r:" % filename
#tells the program to read txt with no parameters 
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

#print txt_again.readlines()
print txt_again.read()

#txt.close()
txt_again.close()

#Keep working on this, especially with closing files!!