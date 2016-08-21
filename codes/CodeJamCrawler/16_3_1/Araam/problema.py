alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def max_party(parties):
	max_p = str(list(parties.keys())[0])
	print(max_p)
	for party in parties:
		print party
		print parties[party]
		if parties[party] > parties[max_p]:
			print("Hello")
			print ("{} > {}".format(parties[party], parties[max_p]))
			max_p = party
	return max_p

def no_majority(parties, num_senators):
	num_s = float(num_senators)
	for party in parties:
		if parties[party] / float(num_s) > 1/float(2):
			return party, False 
	return None, True

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		with open('output.txt', 'w') as o:
			num_cases = int(f.readline())
			for case in range(1, num_cases + 1):
				answer = []
				num_parties = int(f.readline())
				print (num_parties)
				numbers = list(map(int, f.readline().split(' ')))
				parties = {alphabet[i]:numbers[i] for i in range(len(numbers))}
				print (parties)
				num_senators = sum(numbers)
				while num_senators > 0:
					senators_removed = ''
					party_to_remove = max_party(parties)
					print (parties)
					parties[party_to_remove] -= 1
					num_senators -= 1
					senators_removed = party_to_remove
					if (parties[party_to_remove] == 0):
						del parties[party_to_remove]
					other_party, no_major = no_majority(parties, num_senators)
					if not no_major:
						senators_removed += other_party
						parties[other_party] -= 1
						num_senators -= 1
						if (parties[other_party] == 0):
							del parties[other_party]
					print (senators_removed)
					answer.append(senators_removed)
				answer = ' '.join(answer)
				o.write("Case #{}: {}\n".format(case, answer))
			o.close()