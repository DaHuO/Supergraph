import sys

def when_sleep(start_num):
	digits = {}
	digit_count = 0
	sleep_num = -1
	i = 1

	if start_num > 0:	
		while sleep_num == -1:
			next_num = (i*start_num)
			curr_num = next_num
			while curr_num > 0:
				digit = curr_num%10
				curr_num /= 10
				if not digits.get(digit):
					digits[digit] = 1
					digit_count += 1
					if digit_count == 10:
						sleep_num = next_num
						break
			i += 1

	return sleep_num
			

def main():
	n = int(raw_input())

	for i in range(n):
		start_num = int(raw_input())
		sleep_num = when_sleep(start_num)
		if sleep_num == -1:
			print "Case #%d: INSOMNIA" %(i+1)
		else:
			print "Case #%d: %d" %(i+1, sleep_num)
		

if __name__ == "__main__":
	main()
