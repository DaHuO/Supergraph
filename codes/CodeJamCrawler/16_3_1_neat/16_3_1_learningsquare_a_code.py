def solve_case(final_state):

	move_list = []
	current_state = []
	for i in range(len(final_state)):
		current_state.append(0)

	while is_done(current_state, final_state) == False:
		current_state, move = find_move(current_state, final_state)
		move_list.append(move)
		if has_majority(current_state, final_state):
			print 'UH OH'

	return print_moves(move_list)

def remaining(current_state, final_state):
	members_remaining = []
	for i in range(len(current_state)):
		members_remaining.append(final_state[i] - current_state[i])

	return members_remaining

def remaining_sum(current_state, final_state):

	return sum(remaining(current_state, final_state))

def max_parties(current_state, final_state):
	max_parties_list = []
	members_remaining = remaining(current_state, final_state)
	max_members = max(members_remaining)
	for i in range(len(members_remaining)):
		if members_remaining[i] == max_members:
			max_parties_list.append(i)

	return max_parties_list

def find_move(current_state, final_state):
	new_state = current_state[:]
	max_parties_list = max_parties(current_state, final_state)
	if len(max_parties_list) == 1:
		if max(remaining(current_state, final_state)) == 2:
			new_state[max_parties_list[0]] += 2
			move = [max_parties_list[0], max_parties_list[0]]
		elif remaining_sum(current_state, final_state) % 2 == 0:
			new_state[max_parties_list[0]] += 2
			move = [max_parties_list[0], max_parties_list[0]]
		else:
			new_state[max_parties_list[0]] += 1
			move = [max_parties_list[0]]
	if len(max_parties_list) > 1:
		if remaining_sum(current_state, final_state) % 2 == 1:
			new_state[max_parties_list[0]] += 1
			move = [max_parties_list[0]]
		else:
			new_state[max_parties_list[0]] += 1
			new_state[max_parties_list[1]] += 1
			move = [max_parties_list[0], max_parties_list[1]]

	return new_state, move

def is_done(current_state, final_state):
	done = True
	for item in remaining(current_state, final_state):
		if item > 0:
			done = False

	return done

def print_moves(move_list):
	final_moves = []
	party_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for move in move_list:
		print_move = ''
		for item in move:
			print_move += party_names[item]
		final_moves.append(print_move)

	return ' '.join(final_moves)

def has_majority(current_state, final_state):
	majority = False
	for item in remaining(current_state, final_state):
		if remaining_sum(current_state, final_state) > 0:
			if item * 1.0 / remaining_sum(current_state, final_state) > 0.5:
				majority = True

	return majority