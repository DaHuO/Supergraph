def flip(input_s):
  res = ''
  while len(input_s)>0:
    cur = input_s[-1:]
    input_s = input_s[:-1]
    #print 'cur is: ', cur
    #print 'input_s left is: ', input_s
    if (cur=='+'):
      res = '-' + res
    else:
      res = '+' + res
    #print 'res is: ', res
    #print '==='
  return res

def algo(pan):
  count = 0
  pan_len = len(pan)
  for i in xrange(pan_len-1,-1,-1):
    if pan[i] == '-':
      #print 'before: ', pan
      pan = flip(pan[:i+1]) + pan[i+1:]
      count += 1
      #print 'after: ', pan
  return count


def read_then_print(input_file, output_file):
  i = 0
  with open(input_file) as input:
    with open(output_file, 'w') as output:
      for line in input:
        i+=1
        if (i>1): # because the first line is ignored, it's not a value for test-case
          #print '---'
          res = algo(line)
          output.write('Case #' + str(i-1) + ': ' + str(res) + '\n')
        #output.close()


#print flip('-+')
#read_then_print('example_input.txt', 'example_output.txt')
#read_then_print('B-small-attempt0.in', 'output_real.txt')
read_then_print('B-large.in', 'output_real.txt')