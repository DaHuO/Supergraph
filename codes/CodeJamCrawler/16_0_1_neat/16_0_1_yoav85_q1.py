def count(input):
  numbers = [0,1,2,3,4,5,6,7,8,9]
  last = []
  multip = 1
  digits_previous = []
  inso_count = 0
  while len(numbers)>0: #and multip<20:
    digits_current = []
    cur = input * multip
    #print 'multip is: ', multip
    while cur > 0:
      #print 'cur is: ', cur
      digit = cur % 10
      cur = cur / 10
      #print 'digit is: ', digit
      digits_current.append(digit)
      if digit in numbers:
        #print '!'
        numbers.remove(digit)
      if len(numbers)==0:
        break
    multip += 1
    if set(digits_current) == set(digits_previous):
      inso_count += 1
    else:
      inso_count = 0
    if inso_count > 10:
      return 'INSOMNIA'
    digits_previous = digits_current
    #print 'numbers remaining: ', numbers
    #print multip, numbers

  #return multip-1
  return (multip-1) * input


def read_then_print(input_file, output_file):
  i = 0
  with open(input_file) as input:
    with open(output_file, 'w') as output:
      for line in input:
        i+=1
        if (i>1): # because the first line is ignored, it's not a value for test-case
          res = count(int(line))
          output.write('Case #' + str(i-1) + ': ' + str(res) + '\n')
        #output.close()


#read_then_print('input.txt', 'output.txt')
read_then_print('A-large.in', 'output_real.txt')