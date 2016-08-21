import sys

try: 
	f = open(sys.argv[1])
	out = open(sys.argv[1].rpartition("\\")[2]+".out", 'w')

	numTests = int(f.readline())

	for i in range (0, numTests):
		note = f.readline()
	#	print (note)
		
		phoneNo = ""

		zeros = note.count("Z")

#		print ("found zeros: " + str(zeros))

		twos = note.count("W")
#		print ("found twos: " + str(twos))


		fours = note.count("U")

		sixes = note.count("X")

		eights = note.count("G")

		ones = note.count("O") - twos - fours - zeros

		threes = note.count("H") - eights

		fives = note.count("F") - fours

		sevens = note.count("V") - fives

		nines = note.count("I") - fives - sixes - eights

		phoneNo = ("0" * zeros) + ("1" * ones) + ("2" * twos) + ("3"*threes)+("4"*fours)+("5"*fives)+("6"*sixes)+("7"*sevens)+("8"*eights)+("9"*nines)


		
		out.write("Case #" + str(i+1) +": " + phoneNo + "\n")


except IOError as e:
	print ('Error:', err) 

