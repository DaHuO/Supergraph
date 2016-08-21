def algo(count, data):
  parties = []
  datas = data.split(" ")
  for d in datas:
    parties.append(int(d))
  res = ""
  while (1>0):
    #print '===='
    #print parties

    biggest = -1
    biggest_value = -1
    second_biggest = -1
    second_biggest_value = -1
    total_count = 0
    parties_remain_count = 0
    for x in xrange(0,len(parties)):
      if (parties[x] > biggest_value):
        second_biggest = biggest
        second_biggest_value = biggest_value
        biggest = x
        biggest_value = parties[x]
      elif parties[x] > second_biggest_value:
        second_biggest = x
        second_biggest_value = parties[x]
      total_count += parties[x]
      if (parties[x] > 0):
        parties_remain_count += 1
    if (total_count==0):
      return res

    #sanity
    if (total_count/2 < biggest_value):
      print 'total: ' + str(total_count) + " | biggest count: " + str(biggest_value)

    if (total_count/2 <= biggest_value and biggest_value != second_biggest_value):
      if (biggest_value > 1):
        res += chr(65+biggest) + chr(65+biggest) + " " #ord('A') == 65
        parties[biggest] -= 2
      else:
        res += chr(65+biggest) + " "
        parties[biggest] -= 1
    else:
      if (biggest_value==1 and parties_remain_count > 2):
        res += chr(65+biggest) + " "
        parties[biggest] -= 1
      else:
        res += chr(65+biggest) + chr(65+second_biggest) + " "
        parties[biggest] -= 1
        parties[second_biggest] -= 1



def read_then_print(input_file, output_file):
  i = 0
  with open(input_file) as input:
    with open(output_file, 'w') as output:
      cases_count = int(input.readline())
      for x in xrange(1,cases_count+1):
        #print 'case #' + str(x)
        parties_count = int(input.readline())
        parties_data = input.readline()
        res = algo(parties_count, parties_data)
        output.write('Case #' + str(x) + ': ' + str(res) + '\n')


#read_then_print('input1_test.txt', 'output1_test.txt')
#read_then_print('A-small-attempt1.in', 'A-small-attempt1.out')
read_then_print('A-large.in', 'A-large.out')