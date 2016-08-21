import sys


def main():

	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
	  x = [int(s) for s in raw_input().split(" ")]
	  n = x[0];
	  if (n==0):
	  	final="INSOMNIA";
	  else:	
	  	  numbers_seen=[];	  
		  num_in_str=str(n);
		  count=0;
		  final="";
		  slept=0;
		  while (not slept):
			  number_len=len(num_in_str);
			  for x in range(0,number_len):
			  	number=num_in_str[x];
			  	if number not in numbers_seen:
			  		numbers_seen.extend([number]);
			  count=count+1;
			  g=int(num_in_str)
			  prev_g=g;
			  g=n*(count+1);
			  num_in_str=str(g);
			  if (len(numbers_seen)==10:
			  	slept=1;
	   			final=str(prev_g);
	   			break;	   	  

	  print "Case #{}: {}".format(i,final)


if __name__ == "__main__":
	main()