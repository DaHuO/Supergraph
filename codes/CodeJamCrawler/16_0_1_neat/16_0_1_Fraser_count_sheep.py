def process_count_sheep():
  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
  # This is all you need for most Google Code Jam problems.
  file = open('data4.txt','r')
  my_results = open('results.txt','w')
  t = int(file.readline())  # read a line with a single integer
  for i in range(1, t + 1):
    n = int(file.readline().strip('\n')) # read an integer
    print("Case #{}: {}\n".format(i, count_sheep(n)))
    my_results.write("Case #{}: {}\n".format(i, count_sheep(n)))
    # check out .format's specification for more formatting options
  my_results.close()
  file.close()

def count_sheep(n):
  if n == 0:
    return "INSOMNIA"
  number_pile = ''
  bools = [False, False, False, False, False, False, False, False, False, False]
  i = 0
  while(False in bools):
    i += 1
    number_pile += str(i*n)
    for j in range(10):
      if str(j) in number_pile:
        bools[j] = True
  return i*n

process_count_sheep()