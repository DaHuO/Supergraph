#!/usr/bin/python
import sys


def produce_last_word(s):
	result = ''
	for i, c in enumerate(s):
		if c != '\n':
			if i == 0:
				result += c
			else:
				if c >= result[0]:
					result = c + result
				else:
					result = result + c
	return result

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		content = f.readlines()

    	for i in range(0, len(content)):
    		if i > 0:
    			result = produce_last_word(content[i])
    			print("Case #" + str(i) + ": " + result)

