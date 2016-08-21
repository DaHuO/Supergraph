
# void printAnswer(int order, int answer) {
# 	cout << "Case #" << order << ": " << answer << endl;
# }

# // string to2(int)

# long long to10(string base2) {
# 	long long acc;
# 	for(int i = base2.size() - 1; i >= 0; i++) {
# 		acc += base2[i] * pow(2, i);
# 	}

# 	return acc;
# }

# int main() {
# 	int total_num;
# 	cin >> total_num;
# 	for(int m = 1; m <= total_num; m++) {
# 		string str;
# 		cin >> str;

# 		string tmp = str;
# 	}
# }

import math

def toBase10(base2, base):
	accu = 0;
	counter = 0;
	for d in base2:
		accu = accu+ int(d)*pow(2, counter)
		counter = counter + 1
	return accu

def isNotPrime(num):
	for a in range(3, 100000):
		if((num % a) == 0):
			return [True,a]  

	return [False, -1] 

def printAnswer(li):
	print "Case #1:"
	for a in li:
		print "%s %r %r %r %r %r %r %r %r %r" % (a[0], a[1][0], a[1][1], a[1][2], a[1][3],a[1][4],a[1][5],a[1][6],a[1][7], a[1][8])

def main(): 
	outLen = 32;
	outNum = 500;

	li = []

	# start = 32767 
	start = 2147483647
	# start = 33 
	counter = 0;
	while(True):
		counter = counter + 1
		# print len(li)
		start = start + 2;
		base2 = bin(start)[2:]
		# print base2

		# print start
		# print base2
		# print len(base2)
		notPrime = True
		liprime = []
		for b in range(2, 11):
			# print b
			tmp = isNotPrime(int(base2, b))
			if(not tmp[0]):
				break;
			else:
				liprime.append(tmp[1])

		if(len(liprime) == 9):
			li.append([base2, liprime])

		if(len(li) == outNum):
			break;

	printAnswer(li)

main()
