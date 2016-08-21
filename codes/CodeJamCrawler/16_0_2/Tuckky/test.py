#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):

		ans_max_plus = 99
		ans_count_plus = 99
		ans_max_minus = 99
		ans_count_minus = 99

		cipher_input = raw_input()
		
		# max +
		cipher = cipher_input
		idx = len(cipher)
		for character in reversed(cipher):
			if character == '+':
				idx -= 1
			else:
				break

		result = cipher[:idx]
		cipher = cipher[:idx]

		answer = ''
		for i in range(0, len(cipher)):
			answer = '%s+' % answer

		times = 0

		happy = cipher.count('+')
		blank = cipher.count('-')

		_cha = '+' 
		last_seq = '+++++++++++++++++++'
		
		possible_new_cipher = [cipher]

		while True:
			# print possible_new_cipher
			if answer in possible_new_cipher or '' in possible_new_cipher:
				ans_max_plus = times
				break

			_possible_new_cipher = []
			for cipher in possible_new_cipher:
				max_change = {}

				for i in range(1, len(cipher)+1):
					choose = i
					new_cipher = ''
					for character in reversed(cipher[:choose]):
						if character == '+':
							character = '-'
						else:
							character = '+'
						new_cipher = '%s%s' % (new_cipher, character)

					for character in cipher[choose:]:
						new_cipher = '%s%s' % (new_cipher, character)

					if new_cipher == cipher:
						max_change[i] = -1
						continue

					happy = new_cipher.count('+')
					blank = new_cipher.count('-')
					max_ = abs(happy - blank)

					score = 1
					max_change[i] = score

				max_key = max(max_change.iteritems(), key=operator.itemgetter(1))[1] 
				# print max_key
				# print times, '------------------'
				for key, val in max_change.iteritems():
					if val == max_key:
						new_cipher = ''
						for character in reversed(cipher[:key]):
							if character == '+':
								character = '-'
							else:
								character = '+'
							new_cipher = '%s%s' % (new_cipher, character)

						for character in cipher[key:]:
							new_cipher = '%s%s' % (new_cipher, character)

						idx = len(new_cipher)
						for character in reversed(new_cipher):
							if character == _cha:
								idx -= 1
							else:
								break

						new_cipher = new_cipher[:idx]
						if not new_cipher in _possible_new_cipher:
							_possible_new_cipher.append(new_cipher)
						# print new_cipher
				# print times, _possile_new_cipher, new_cipher

			possible_new_cipher = _possible_new_cipher 
			times += 1
			if times >= ans_max_plus:
				break
	
		# # max -
		# cipher = cipher_input
		# idx = len(cipher)
		# for character in reversed(cipher):
		# 	if character == '-':
		# 		idx -= 1
		# 	else:
		# 		break

		# result = cipher[:idx]
		# cipher = cipher[:idx]

		# answer = ''
		# for i in range(0, len(cipher)):
		# 	answer = '%s-' % answer

		# times = 0

		# happy = cipher.count('+')
		# blank = cipher.count('-')

		# _cha = '-' 
		# last_seq = '-------------------'
		
		# possible_new_cipher = [cipher]

		# while True:
		# 	if answer in possible_new_cipher or '' in possible_new_cipher:
		# 		ans_max_minus = times + 1
		# 		break

		# 	_possible_new_cipher = []
		# 	for cipher in possible_new_cipher:
		# 		max_change = {}

		# 		for i in range(1, len(cipher)+1):
		# 			choose = i
		# 			new_cipher = ''
		# 			for character in reversed(cipher[:choose]):
		# 				if character == '+':
		# 					character = '-'
		# 				else:
		# 					character = '+'
		# 				new_cipher = '%s%s' % (new_cipher, character)

		# 			for character in cipher[choose:]:
		# 				new_cipher = '%s%s' % (new_cipher, character)

		# 			if new_cipher == cipher:
		# 				max_change[i] = -1
		# 				continue

		# 			happy = new_cipher.count('+')
		# 			blank = new_cipher.count('-')
		# 			max_ = abs(happy - blank)

		# 			score = max_
		# 			max_change[i] = score

		# 		max_key = max(max_change.iteritems(), key=operator.itemgetter(1))[1] 
		# 		for key, val in max_change.iteritems():
		# 			if val == max_key:
		# 				new_cipher = ''
		# 				for character in reversed(cipher[:key]):
		# 					if character == '+':
		# 						character = '-'
		# 					else:
		# 						character = '+'
		# 					new_cipher = '%s%s' % (new_cipher, character)

		# 				for character in cipher[key:]:
		# 					new_cipher = '%s%s' % (new_cipher, character)

		# 				idx = len(new_cipher)
		# 				for character in reversed(new_cipher):
		# 					if character == _cha:
		# 						idx -= 1
		# 					else:
		# 						break
		# 				new_cipher = new_cipher[:idx]
		# 				if not new_cipher in possible_new_cipher:
		# 					_possible_new_cipher.append(new_cipher)

		# 	possible_new_cipher = _possible_new_cipher 
		# 	times += 1
		# 	if times >= ans_max_minus:
		# 		break
	
		ans = min(ans_max_plus, ans_count_plus, ans_max_minus, ans_count_minus)
		print("Case #%i: %s" % (caseNr, (ans)))