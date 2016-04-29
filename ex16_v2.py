from sys import argv

script, filename = argv


print "Opening file %s for write." % filename
print "Press CTRL+C (^c) to stop."


f = open(filename, 'w')

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "Writing lines to file."
f.write(line1+"\n"+line2+"\n"+line3)
f.close()
