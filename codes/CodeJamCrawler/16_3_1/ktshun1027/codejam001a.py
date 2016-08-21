# -*- coding:utf-8 -*-
from string import uppercase
if __name__ == "__main__":
	caseNum = input()
	for i in xrange(caseNum):
		partyNum = input()
		member = map(int,raw_input().split())
		ans = []
		while sum(member) > 0:
			maxparty = [0,0]
			maxparty[0] = max(enumerate(member), key = lambda member: member[1])[0]
			member[maxparty[0]] -= 1
			if sum(member) != 0:
				maxparty[1] = max(enumerate(member), key = lambda member: member[1])[0]
				member[maxparty[1]] -= 1
			if max(member) > (sum(member) / 2.0) and sum(member) != 0:
				member[maxparty[1]] += 1
				ans.append(uppercase[maxparty[0]])
			else:
				ans.append(uppercase[maxparty[0]] + uppercase[maxparty[1]])
		print "Case #" + str(i+1) + ": " + " ".join(ans)




