import sys


def main():
	# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
 	# script,filename=argv;
 	# file=open(filename)
 	# print file.read()

	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
	  x = [int(s) for s in raw_input().split(" ")]
	  n = x[0];
	  if (n!=0):
		  numbers_seen=[];	  
		  numbers_all=["0","1","2","3","4","5","6","7","8","9"]
		  num_in_str=str(n);
		  count=0;
		  final="";
		  slept=False;
		  while (not slept):
		  	  # print num_in_str
			  number_len=len(num_in_str);

			  for x in range(0,number_len):
			  	number=num_in_str[x];
			  	# print number
			  	if number not in numbers_seen:
			  		numbers_seen.extend([number]);
			  count=count+1;
			  g=int(num_in_str)
			  prev_g=g;
			  g=n*(count+1);
			  num_in_str=str(g);
			  # print num_in_str
			  # print numbers_seen

			  if (len(numbers_seen)==len(numbers_all)):

			  	# print "sleeping"
			  	slept=True;
	   			final=str(prev_g);
	   			break;
	  else:	
	   	  final="INSOMNIA";

	  print "Case #{}: {}".format(i,final)
	  # check out .format's specification for more formatting options

if __name__ == "__main__":
	main()