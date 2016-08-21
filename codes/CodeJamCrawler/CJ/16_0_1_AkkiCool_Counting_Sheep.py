from array import array

file_read = open('A-small-attempt0.in', 'r')
file_write = open('output.in', 'w')

p = file_read.readline()

for i in range(int(p)):
	value = file_read.readline()
	increment = 1
	file_write.write("Case #"+str(i+1)+":")

	if int(value) == 0:
		file_write.write(" INSOMNIA\n")
	else:
		a = array("c")
		
		while (1):
			value1 = str(int(value) * increment)
			length = len(value1)
			for j in range(length):
				sigle_char = value1[j]
				# print "sigle_char"+str(sigle_char)
				if sigle_char in a:
					print ''
				else:
					# print 'value ist : '+str(sigle_char)
					a.append(sigle_char)

			if len(a) == 10:
				file_write.write(" "+str(value1)+"\n")
				break

			increment = increment + 1