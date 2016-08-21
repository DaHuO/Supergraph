def flip_pancakes(filename_in, filename_out):
	with open(filename_in, 'r') as input_f:
		test_cases = int(input_f.readline());
		for x in range(test_cases):
			faces = input_f.readline().replace('\n','')
			no = len(faces)
			i = 2
			flip_count = 0
			# print "\nfaces begin: ",faces
			# print "len(set(faces)): ", len(set(faces))
			while len(set(faces)) != 1:
				# print "after while faces: ", faces
				if (faces[:i][1:] == faces[:i][:-1]):
					i+=1
				else: 
					if set(faces[:i-1]).pop() == "+":
						# print "replacing %d pluses..."%(i-1)
						faces = faces[:i-1].replace("+","-") + faces[i-1:]
					elif set(faces[:i-1]).pop() == "-":
						# print "replaced %d minuses..."%(i-1)
						faces = faces[:i-1].replace("-","+") + faces[i-1:]
					flip_count += 1
				# print "new stack: %s" %(faces)
			if set(faces).pop() == "-":
				faces = faces.replace("-","+")
				flip_count += 1
				# print "after plusing... "
			# print "i: ", i
			# print "%d no of flips: "%(flip_count)
			# print "test case: ", x+1

 			# print "\nfinal face: %s\n"%(faces)
 			mode = 'a'			
			with open(filename_out,mode) as output_f:
				output_f.write('Case #%d: %s\n' %(x+1,flip_count))

flip_pancakes('B-large.in', 'B-large.out')
 