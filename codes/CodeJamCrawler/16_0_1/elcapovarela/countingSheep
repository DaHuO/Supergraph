f = open("countingSheepLarge.in", "r")
new_file = open("countingSheepLargeSol", "w")
t = int(f.readline())


def last_counted_number (n):
	if n == 0:
		return "INSOMNIA"
	else:
		numbers_seen = set()
		current_number = 0
		while len(numbers_seen) < 10:
			current_number += n
			for i in str(current_number):
				if i not in numbers_seen:
					numbers_seen.add(i)
		return current_number

for i in range(1,t+1):
	n = int(f.readline())
	new_file.write("Case #"+str(i)+ ": "+str(last_counted_number(n))+"\n")

