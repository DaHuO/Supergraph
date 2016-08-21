def fill (number, digits):
	temp = number;

	while (temp):
		digit = temp % 10;
		temp //= 10;
		if (not digit in digits):
			digits.append (digit);

def maxed_out (number):
	if (not number):
		return ('INSOMNIA');

	digits, i = [], 1;
	num = 0;

	while (len (digits) < 10):
		num += number;
		fill (num, digits);
		i += 1;

	return (num);


#cases = [int (input ()) for i in range (int (input ()))];
fobj = open("A-large.in", "r");
cases = [];
count = True;

for line in fobj:
	if (count):
		count = False;
		continue;

	cases.append (int (line));

i = 1;

for case in cases:
	print ('Case #%d:' %(i), maxed_out (case));
	i += 1;