N = 16
J = 50

def binary_string(n):
  if n == 0: return ""
  else: return binary_string(n/2) + str(n%2)

def eleven_divisibility_rule(bin_str):
  even_sum = sum(int(x) for x in bin_str[::2])
  odd_sum = sum(int(x) for x in bin_str[1::2])
  last_digit = int(bin_str[-1])
  return even_sum == odd_sum and last_digit
  
print_string = "Case #1:\n"
number_of_solutions = 0
for i in range(2**(N-1)+1, 2**(N)):
  coin = binary_string(i)
  if eleven_divisibility_rule(coin):
    print_string += "%s 3 4 5 6 7 8 9 10 11\n"%coin
    number_of_solutions += 1
    if number_of_solutions == J:
      break

print print_string
