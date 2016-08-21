def main():
	T=input()
	for t in range(T):
		seq=raw_input()
		new_seq=seq
		num_flips=0
		while 1:
			right_most_neg=-1
			for i in range(len(new_seq)):
				if new_seq[i]=="-":
					right_most_neg=i

			if right_most_neg==-1:
				break
			temp=""
			for i in range(right_most_neg+1):
				if new_seq[i]=="+":
					temp+="-"
				else:
					temp+="+"
			num_flips+=1
			for i in range(right_most_neg+1,len(new_seq)):
				temp+=new_seq[i]
			new_seq=temp
		print "Case #"+str(t+1)+": "+str(num_flips)


if __name__=="__main__":
	main()