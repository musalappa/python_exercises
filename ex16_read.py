from sys import argv

script, filename = argv

file = open(filename, 'r')

line1 = file.readline()
print line1

line2 = file.readline()
print line2

line3 = file.readline()
print line3

file.close()
