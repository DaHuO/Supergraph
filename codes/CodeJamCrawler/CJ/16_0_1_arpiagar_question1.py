def count_sleep_times(num):
    count = 0
    init_map = {}
    counter = 1
    number =  num
    if num == 0:
      return 'INSOMNIA'
    while True:
      string_array =  str(number)
      for elem in string_array:
        if not init_map.has_key(elem):
          init_map[elem] =  True
          count += 1
      counter += 1
      if count == 10:
        return str(number)
      number += num



if __name__ == "__main__":
  filepath = raw_input().strip()
  f = open(filepath, 'rb')
  out  =  open('output.txt','wb')
  flag = True
  for lines in f:
    if flag:
      n =  lines
      flag = False
      count = 1
      continue
    elem =  int(lines.strip())
    out.write("Case #"+str(count)+": "+count_sleep_times(elem))
    out.write('\n')
    count += 1
  out.close()
  f.close()