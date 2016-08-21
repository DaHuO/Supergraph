def flip( n, index ):
  m = ""
  # if index == 0 and '-' in n[0]:
  #   return "+" + n[1:]
  for x in reversed(range(0,index + 1)):
    # print "in fcn (x): ", x
    if '+' in n[x]:
      m = m + "-"
    else:
      m = m + "+"
  return m + n[index+ 1:]

def checkAll( n ):
  for x in range(0, len(n)):
    if "-" in n[x]:
	  return False
  return True
	

def calculateFlips(n, index, count):
  if checkAll(n):
  	return count
  elif index >= 0 and index < len(n):
    new = flip(n, index)
    x = calculateFlips(new, index + 1, count + 1)
    y = calculateFlips(n, index + 1, count)
    return min(x, y)
  else:
  	return 10000

def main():
  input_file = open('B-small-attempt0.in')
  lines = input_file.readlines()
  output_file = open("myoutput.txt", "w")
  
  for line_number in range(1, len(lines)): #loop over all inputs
    plus_minus_string = lines[line_number].strip() #take one input at a time
    times = calculateFlips(plus_minus_string, 0, 0)


    # print
    # print "the string: ", plus_minus_string
    # if not checkAll(plus_minus_string):
    #   if '-' in plus_minus_string[0]:
      # output_file.write('Case #' + str(line_number) + ': ' +  times + "\n")
      # for i in reversed( range(0,len(plus_minus_string)) ): # for the length of that n
      #   # print "the string: ", plus_minus_string
      #   if '-' in plus_minus_string[i]:
      #     print "string flipped at: ", i
      #     plus_minus_string = flip(plus_minus_string, i )
      #     print "flipped string: ", plus_minus_string
      #     times = times + 1
    
    # output_file.write("string: " + plus_minus_string + "\n")
    output_file.write('Case #' + str(line_number) + ': ' +  str(times) + "\n")
    # string = 'Case #' + str(line_number) + ': ' +  new + "\n"
    # output_file.write(string)
  output_file.close()

if __name__ == '__main__':
	main()
