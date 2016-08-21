def get_flips(s):
  # first check if all + or -
  if s.find("-") == -1:
    return 0
  if s.find("+") == -1:
    return 1

  # otherwise, loop through and count
  count = 0
  for i in range(1, len(s)):
    if s[i] != s[i-1]:
      count += 1

  # add extra for even flips and - in front
  if s[0] == '-' and count % 2 == 0:
    count += 1
  elif s[-1] == '-' and count % 2 == 1:
    count += 1

  return count

try:
  # open the file for reading
    input_file = open("B-large.in", 'r')
    output_file = open("B-large.out", 'w')

except IOError:
  print("Error reading or writing to file")
else:
    t = int(input_file.readline())
  # loop through the input
    for case_num in range(0, t):

        s = input_file.readline().rstrip()
        s = s.rstrip('+')

        # write to file
        output_file.write("Case #" + str(case_num+1) + ": " + str(get_flips(s)) + "\n")

finally:
    input_file.close()
    output_file.close()
