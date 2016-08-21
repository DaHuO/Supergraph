#!/usr/bin/python

def bitstring(num):
  if num < 0:
    num = -i

  result = 0
  while num > 0:
    result = result | 1 << (num%10)
    num = num/10

  return result

def process_input(N):
  current_value = N
  current_bitstring = bitstring(current_value)
  i = 1
  
  inactivity_counter = 0
  
  while current_bitstring != 0b1111111111 and inactivity_counter < 10:
    i += 1
    next_value = current_value + N
    next_bitstring = bitstring(next_value)

    if next_bitstring ^ current_bitstring is 0:
      inactivity_counter += 1
    else:
      inactivity_counter = 0

    current_value = next_value
    current_bitstring |= next_bitstring
    
  if inactivity_counter >= 10:
    return 'INSOMNIA'

  return str(current_value)

def main():
  T = int(raw_input())
  for t in range(1, T +1):
    N = int(raw_input())
    result = process_input(N)
    print 'Case #' + str(t) + ': ' + result

if __name__ == '__main__':
  main()

    