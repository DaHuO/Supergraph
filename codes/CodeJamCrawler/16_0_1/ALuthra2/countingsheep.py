def duplicate(arr):
	counter = 0;
	arr.sort();
	while (counter < len(arr)-1):
		if arr[counter] == arr[counter + 1]:
			arr.remove(arr[counter]);
			counter = counter - 1;
		counter = counter + 1;
	return arr;

def countingSheep(n):
	end = "INSOMNIA"
	counter1 = 1;
	arr1 = [];
	arr1.append(2);
	arr2 = [];
	arrans = [0,1,2,3,4,5,6,7,8,9];
	
	if (n == 0):
		return end;
	else:
		while(arr1 != arrans):
			n2 = counter1 * n;
			arr2 = list(str(n2));
			arr2 = map(int, arr2);
			arr2.sort();
			arr1.sort();
			for x in arr2:
				arr1.append(x);
			arr1.sort();
			duplicate(arr1);
			arr1.sort();
			if arr1 == arrans:
				return n2;
			counter1 = counter1 + 1;

#Main
readfile = open("A-small-attempt11.in", 'r');
number = readfile.readlines();
writefile = open("test.txt", 'w');
counter = 1;
counter2 = int(number[0]);
while (counter <= counter2):
	y = countingSheep(int(number[counter]));
	if y == None:
		 writefile.write("Case #" + str(counter) + ": INSOMNIA\n");
	else:
		writefile.write("Case #" + str(counter) + ": " + str(y) + "\n");
	counter = counter + 1;

