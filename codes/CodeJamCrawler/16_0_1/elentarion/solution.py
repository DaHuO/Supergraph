nb_test_cases = int(raw_input())

masks = [
  0b0000000001,
  0b0000000010,
  0b0000000100,
  0b0000001000,
  0b0000010000,
  0b0000100000,
  0b0001000000,
  0b0010000000,
  0b0100000000,
  0b1000000000,
]

for case_number in range(1, nb_test_cases + 1):
  mask = 0b0000000000
  i = 1
  initial_n = int(raw_input())
  insomnia = False
  while True:
  	n = initial_n * i
  	
  	digits = str(n)
  	for digit in digits:
  	  mask = mask | masks[int(digit)]
  	
  	if n == initial_n and i != 1:
  	  insomnia = True
  	  break
  	elif mask == 1023:
  	  break
  		
  	i += 1
  
  if insomnia:
  	print 'Case #%d: INSOMNIA' % (case_number)
  else:
  	print 'Case #%d: %d' % (case_number, n)
  	
  case_number += 1