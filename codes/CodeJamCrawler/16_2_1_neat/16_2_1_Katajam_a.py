
from collections import defaultdict

N = int(input())
for i in range(N):
	data = {}; cnt = ''; count = 0
	s = list(input()); length = len(s); nums = []

	# print('s is', s)
	for x in s:
		if x not in data: data[x] = 1
		else: data[x] += 1
	# print(data)

	if 'Z' in data and data['Z'] != 0: 
		n_zero = data['Z']
		cnt += '0'*n_zero; count += n_zero
		data['E'] -= n_zero
		data['R'] -= n_zero
		data['O'] -= n_zero
		if count == length: continue

	if 'X' in data and data['X'] != 0:
		n_six = data['X']
		cnt += '6'*n_six; count += n_six
		data['S'] -= n_six
		data['I'] -= n_six
		if count == length: continue

	if 'S' in data and data['S'] != 0:
		n_seven = data['S']
		cnt += '7'*n_seven; count += n_seven
		data['E'] -= n_seven*2
		data['V'] -= n_seven
		data['N'] -= n_seven
		if count == length: continue

	if 'U' in data and data['U'] != 0:
		n_four = data['U']
		cnt += '4'*n_four; count += n_four
		data['F'] -= n_four
		data['O'] -= n_four
		data['R'] -= n_four
		if count == length: continue

	if 'G' in data and data['G'] != 0:
		n_eight = data['G']
		cnt += '8'*n_eight; count += n_eight
		data['E'] -= n_eight
		data['I'] -= n_eight
		data['H'] -= n_eight
		data['T'] -= n_eight
		if count == length: continue

	if 'W' in data and data['W'] != 0:
		n_two = data['W']
		cnt += '2'*n_two; count += n_two
		data['T'] -= n_two
		data['O'] -= n_two
		if count == length: continue

	if 'V' in data and data['V'] != 0:
		n_five = data['V']
		cnt += '5'*n_five; count += n_five
		data['F'] -= n_five
		data['I'] -= n_five
		data['E'] -= n_five
		if count == length: continue

	if 'O' in data and data['O'] != 0:
		n_one = data['O']
		cnt += '1'*n_one; count += n_one
		data['N'] -= n_one
		data['E'] -= n_one
		if count == length: continue

	if 'I' in data and data['I'] != 0:
		n_nine = data['I']
		cnt += '9'*n_nine; count += n_nine
		data['N'] -= n_nine*2
		data['E'] -= n_nine
		if count == length: continue

	if 'T' in data and data['T'] != 0:
		n_three = data['T']
		cnt += '3'*n_three; count += n_three
		data['H'] -= n_three
		data['E'] -= n_three*2
		data['R'] -= n_three
		if count == length: continue

	# print(data)
	print('Case #{}: {}'.format(i+1, ''.join(sorted(cnt))))
	# print(cnt)