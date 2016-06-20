import os
from file_search import gci

def main():
	f = gci('./codes')
	file_out = open('record.txt', 'w')
	for File in f:
		fileName = File.split('/')[-1]
		if 'sort' in fileName and fileName[-3:] == '.py':
			file_out.write(File + '\n')
	file_out.close()

if __name__ == '__main__':
	main()