from string import ascii_uppercase as LETTERS
from math import ceil

def validate_senate(senates_dict, n):
	if n == 1:
		return False
	half = int(ceil(n*1./2))
	if half + 1 in senates_dict:
		return False
	else:
		return True

def add_senate(senates_dict, key, party):
	if key > 0:
		senates_dict[key].remove(party)
		if not senates_dict[key]:
			senates_dict.pop(key)
	new_key = key + 1
	if new_key in senates_dict:
		senates_dict[new_key].append(party)
	else:
		senates_dict[new_key] = [party]

def remove_senate(senates_dict, key, party):
	senates_dict[key].remove(party)
	if not senates_dict[key]:
		senates_dict.pop(key)
	new_key = key - 1
	if new_key == 0:
		return
	if new_key in senates_dict:
		senates_dict[new_key].append(party)
	else:
		senates_dict[new_key] = [party]

def trace_route(N, senates):
	escape = []
	senates_dict = {}
	n = 0
	for i in xrange(N):
		if senates[i] not in senates_dict:
			senates_dict[senates[i]] = [LETTERS[i]]
		else:
			senates_dict[senates[i]].append(LETTERS[i])
		n += senates[i]
	
	while senates_dict:
		max_parties_n = max(senates_dict.keys())
		max_parties = senates_dict[max_parties_n]
		escape_step = max_parties[0]
		remove_senate(senates_dict, max_parties_n, max_parties[0])
		if not senates_dict:
			break
		n -= 1
		if max_parties:
			test = max_parties[0]
		else:
			max_parties_n = max(senates_dict.keys())
			max_parties = senates_dict[max_parties_n]
			test = max_parties[0]
		remove_senate(senates_dict, max_parties_n, test)
		if validate_senate(senates_dict, n - 1):
			n -= 1
			escape_step += test
		else:
			add_senate(senates_dict, max_parties_n - 1, test)
		escape.append(escape_step)
	return escape
		
def solveCase(case, f, fout):
	N = int(f.readline().strip())
	senates = f.readline().strip().split(' ')
	for i in xrange(len(senates)):
		senates[i] = int(senates[i])
	escape = trace_route(N, senates)
	writeLine(fout, case, ' '.join(escape))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = 'A-large.in'
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
