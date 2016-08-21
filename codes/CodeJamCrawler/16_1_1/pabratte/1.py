#!/usr/bin/python
import sys
from itertools import product, permutations

def generateSequences(length):
	return [''.join(x) for x in product(['L', 'G'], repeat=length)]


def transformSequence(seq, origSeq):
	newSeq = ''
	for i in seq:
		if i == 'L':
			newSeq = newSeq + origSeq
		else:
			newSeq = newSeq + 'G'*len(origSeq)
	#sys.stdout.write("transformSequence: %s => %s\n"%(seq, newSeq))
	return newSeq


def transpose(seqs):
	newSeqs = []
	for i in range(0, len(seqs[0])):
		tmp = []
		for seq in seqs:
			tmp.append(seq[i])
		newSeqs.append("".join(tmp))
	return newSeqs


def orSeq(seq1, seq2):
	tmp = []
	for i in range(0, len(seq1)):
		if seq1[i]=='G' or seq2[i]=='G':
			tmp.append('G')
		else:
			tmp.append('L')
	
	return ''.join(tmp) 


if __name__ == '__main__':
	input = open(sys.argv[1])
	output = open(sys.argv[1]+'.out', 'w')

	T = int(input.readline())
	for t in range(0, T):
		result = ''		
		S = input.readline()
		for c in S:
			if result == '':
				result = c
			else:
				if c>=result[0]:
					result = c+ result
				else:
					result = result + c				
		output.write("Case #%i: %s"%(t+1,result))
		
		
			
	input.close()
	output.close()
