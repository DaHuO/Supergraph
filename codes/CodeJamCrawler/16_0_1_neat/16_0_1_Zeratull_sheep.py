
def numer(it,numb):
	num = 0;
	seen = []
	looper = 1;
	if numb == 0:
		return "Case #"+str(it)+": INSOMNIA";
	while not (checker(seen)):
		num = numb*looper;
		# print num;
		while num>=10:	
			remainder = num%10
			num = num/10
			seen.append(remainder); 
		seen.append(num);
		looper = looper + 1;
	return "Case #"+str(it)+": "+str(numb*(looper-1));


def checker(array):
	fromC = [0,1,2,3,4,5,6,7,8,9];
	for x in array:
		if x in fromC:
			fromC.remove(x);
	return (not fromC);





def main():
	numtests = int(raw_input())
	# aray = [1,2,3,4,5,6,7,8,9,0];

	# print aray
	# print checker(aray);

	# print numtests;
	loop = 1




	while loop <= numtests:
		n = int(raw_input())
		print numer(loop,n);
		loop = loop + 1;	



if __name__ == '__main__':
	main();