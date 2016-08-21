def main():
  file = open('A-large.in')
  lines = file.readlines()
  f = open("myoutput.txt", "w")
  for line_number in range(1, len(lines)): #loop over all inputs
    # print "line_number = ", line_number
    n = lines[line_number].strip() #take one n at a time
    dictionary = {} #dictionary for that n
    # print "n: ", n
    if int(n) == 0:
      string = 'Case #'+ str(line_number) +': INSOMNIA\n'
      f.write(string)
    else:
      increment = 1
      new = ""
      while( len(dictionary) < 10 ): # till all numbers are not found
        new = str(int(n) * increment)
        # print "new = ", new    
        
        for i in range(0, len(new) ): # for the length of that n
          # print "length = ", len(new), "   new[", i, "]: ", new[i]
          if not dictionary.has_key( new[i] ):
            dictionary[ new[i] ] = 1
        
        increment = increment + 1 # update the n
	    # print "n after update: ", new
	    # print "dictionary: ", dictionary
      string = 'Case #' + str(line_number) + ': ' +  new + "\n"
      f.write(string)
  f.close()

if __name__ == '__main__':
	main()
