import copy
result = ""
digit_dict = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}

def get_the_digits(s):
	global result
	result = ""
	s = s.rstrip()
	num_s = ""
	count_dict = dict((letter,s.count(letter)) for letter in set(s))
	for i in range(0, 10):
		dfs(count_dict, i, num_s)
	return result

def dfs(count_dict, i, num_s):
	global result
	if check_empty(count_dict) and result == "":
		result = num_s
		return
	for j in range(i, 10):
		backup = copy.deepcopy(count_dict)
		if countains_digit(count_dict, j):
			for char in digit_dict[j]:
				count_dict[char] = count_dict[char] - 1
			dfs(count_dict, j, num_s + str(j))
		count_dict = backup

def countains_digit(count_dict, i):
	backup = copy.deepcopy(count_dict)
	for char in digit_dict[i]:
		if char not in backup or backup[char] == 0:
			return False
		else:
			backup[char] = backup[char] - 1
	return True

def check_empty(count_dict):
	for key, value in count_dict.iteritems():
		if value != 0:
			return False
	return True

if __name__ == "__main__":
    f = open('A-small-attempt0.in', 'r')
    output = open('A-small-attempt0.out', 'w')
    C = int(f.readline())
    for i in range(0, C):
        s = f.readline()
        output.write("Case #" + str(i + 1) + ": " + str(get_the_digits(s)) + "\n")
