import numpy as np
import pandas as pd

class senate:
	reader =0
	noTrials = -1
	n = 1 ## For printing case#n
	letters = -1

	def __init__(self, inputPath):
		self.reader = pd.read_table(inputPath, iterator=True, header=None)
		N = self.reader.get_chunk(1)
		self.noTrials = N.iat[0,0]
		self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	def doTrial(self):
		chunky = self.reader.get_chunk(1)
		no_factions = chunky.iat[0,0]
		factions = np.zeros(no_factions)
		numbery = self.reader.get_chunk(1)
		X = numbery[0].to_string()
		X = X.split()
		X = X[1::]

		for i in range(no_factions):
			factions[i]=int(X[i])

		instructions = np.array([ 0, 0, ])
		##faction n 0 is don't
		
		while np.any(factions):
			if len(np.flatnonzero(factions[factions!=0]))==2 and np.max(factions)==1:
				##Remove the last two
				rc = np.flatnonzero(factions)
				instructions = np.vstack((instructions,[rc[0]+1,rc[1]+1]))
				break
			else:
				##Find any most.
				M = np.max(factions)
				idx = np.where(factions==M)

				factions[idx[0][0]] = factions[idx[0][0]]-1
				Mm= np.max(factions)
				f = factions[::]
				noMax = len(f[f==Mm])

				if noMax>2 or noMax==1:
					idx2 = np.where(factions==Mm)
					##Remove another max
					factions[idx2[0][0]] = factions[idx2[0][0]] -1
					instructions = np.vstack((instructions,[idx[0][0]+1,idx2[0][0]+1]))
				elif noMax==2:
					instructions = np.vstack((instructions,[idx[0][0]+1,0]))
		out = ''
		SH = np.shape(instructions)
		for i in range(0,SH[0]-1):
			out = out + ' ' + self.letters[instructions[i+1][0]-1]
			if instructions[i+1][1]!=0:
				out = out + self.letters[instructions[i+1][1]-1]
			if i !=SH[0]-2:
				out = out

		print('Case #', self.n, ':', out, sep='')
		self.n = self.n+1

if __name__ == '__main__':
	inPath = 'A-small-attempt1.in'
	S = senate(inPath)
	while S.n <=S.noTrials:
		S.doTrial()
