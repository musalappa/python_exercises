from sys import argv

script, from_file, to_file = argv

in_data = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()