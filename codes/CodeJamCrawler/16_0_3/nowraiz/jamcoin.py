import math;

def reverse(string):
	return string[::-1];

def interpretation(num, base):
	power = 0; number = 0;
	for i in reverse(str(num)):
		number = number + (base**power)*int(i);
		power = power + 1;
	return number;

def prime(n):
	root = math.sqrt(math.sqrt(math.sqrt(n)));
	for i in range(2,int(root)):
		if (n%i == 0):
			return str(i);
	return None

# def allOnes(string):
# 	for i in string:
# 		if i != "1":
# 			return False;
# 	return True;

# def alljamcoins(length):
# 	coins = [];
# 	bits = "0"*(length-2);
# 	coins.append("1"+bits+"1")
# 	while not allOnes(bits):
# 		bits = increment(bits);
# 		coins.append("1"+bits+"1")
# 	return coins

def increment(string):
	if (string[-1] == "0"):
		return string[0:len(string)-1]+"1";
	index = len(string)-2;
	final = "0";
	while(string[index] == "1"):
		final = "0" + final;
		index = index-1;
	final = "1" + final;
	index = index-1;
	while(index > -1):
		final = string[index] + final;
		index = index -1;
	return final;

def validjamcoin(jamcoin):
	divisors = [];
	for i in range(2,11):
		inter = interpretation(int(jamcoin),i);
		value = prime(inter)
		if value is not None:
			divisors.append(value)
		else:
			return None;
	return divisors;

def jamcoins(length,count):
	bit = "0"*(length-2);
	# coin = alljamcoins(length);
	i = 0; values = 0;
	totalCoins = 2**(length-2);
	while i < totalCoins and values < count:
		coin = "1" + bit + "1";
		value = validjamcoin(coin);
		if value is not None:
			output = coin;
			output = output + " " + " ".join(value);
			print output;
			values = values + 1;
		i = i+1;
		bit = increment(bit);

if __name__ == '__main__':
	case = int(raw_input())
	for i in range(case):
		string = str(raw_input())
		string = string.split();
		print "Case #"+ str(i+1) + ":"
		jamcoins(int(string[0]),int(string[1]));


