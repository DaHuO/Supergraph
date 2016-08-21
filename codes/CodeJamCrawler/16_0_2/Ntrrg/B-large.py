"""Problem B. Revenge of the Pancakes
		Miguel Angel Rivera Notararigo (ntrrg) <ntrrgx@gmail.com>
"""

def sort(string):
	n = 0

	while "-" in string:
		if string.startswith("-"):
			i = len(string) - string[-1::-1].find("-")
			string = switch(string[:i]) + string[i:]

		else:
			i = 1

			for char in string[1:]:
				if char == "-":
					break

				i += 1

			string = switch(string[:i]) + string[i:]

		n += 1

	return n

def switch(string): 
	return "".join(["+" if char == "-" else "-" for char in string])

input = open("B-large.in")
output = open("output", "w")

T = int(input.readline())
assert T >= 1 and T <= 100

n = 1

while T > 0:
	S = input.readline().strip()
	assert len(S) >= 1 and len(S) <= 100

	for char in S:
		assert char == "+" or char == "-"

	r = sort(S)

	output.write("Case #%i: %s\n" % (n, r))

	T -= 1
	n += 1

input.close()
output.close()