

def jamcoin_to_number(jamstring, base):
  total = 0
  for i, item in enumerate(reversed(list(jamstring))):
    total += (int(item)*base**i)
  return total


def first_factor(num):
  # for i in range(2, int(num**0.5)+1):
  for i in range(2, 100):
    if num % i == 0:
      return i
  return None

# print first_factor(73)


def jamcoin_enumerator(num_digits):
  formatter = "{0:b}"

  for i in xrange(2**(num_digits-2)):
    middle = formatter.format(i)
    if len(middle) < num_digits-2:
      num_extra_zeros = num_digits-2-len(middle)
      middle = ("0"*num_extra_zeros) + middle

    padded = "1" + str(middle) + "1"
    yield padded


def jamcoin_divisors(jamcoin):
  factor_list = []
  for i in range(2, 11):
    num = jamcoin_to_number(jamcoin, i)
    ff = first_factor(num)
    if ff is None:
      return None
    factor_list.append(ff)
  return factor_list



# print jamcoin_divisors("100011")
# print jamcoin_divisors('111111')
# print jamcoin_divisors('111001')


def find_answers(n, j):
  answer_array = []
  a = jamcoin_enumerator(n)
  for thing in a:
    print thing
    divisors = jamcoin_divisors(thing)
    if divisors is not None:
      print divisors
      answer_array.append((thing, divisors))
      if len(answer_array) == j:
        return answer_array

  raise Exception("Could not find ")


# print find_answers(16, 50)


def write_answer(n, j):
  answers = find_answers(n,j)
  filename = "answers_for_n-" + str(n) + "__j-" + str(j) + ".txt"
  f = open(filename, 'w')
  f.write("Case #1:\n")
  for i, l in answers:
    f.write(i)
    for d in l:
      f.write(" " + str(d))
    f.write('\n')
  f.close()


# print jamcoin_to_number('1000000010101001', 6)
# print jamcoin_to_number('1000000010100111', 6)

write_answer(32, 500)

# a = jamcoin_enumerator(16)
# for thing in a:
#   print str(thing) + "  :   "  + str(jamcoin_divisors(thing))


# a = jamcoin_enumerator(6)
# for thing in a:
#   print str(thing) + "  :   "  + str(jamcoin_divisors(thing))

# print jamcoin_divisors("1001")

# a = jamcoin_enumerator(6)
# for things in a:
#   print things
# print a.next()
# print a.next()
# print a.next()







# a = jamcoin_to_number("1001", 5)
# print a
