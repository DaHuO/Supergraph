#!/usr/bin/python
import sys;

T = int(raw_input());

for i in range(T):

	N = int(raw_input());

	senators = map(int, raw_input().strip().split() );
	senatorCount = 0;

	struct = [];
	for j in range(len(senators)):
		senatorCount += senators[j];
		struct.append([senators[j], j]);

	struct.sort(reverse=True);
#	print struct, senatorCount;

	outputStr = "";
	while senatorCount > 0:
		outputStr += chr(ord('A') + struct[0][1]);
		senatorCount -= 1;
		struct[0][0] -= 1;
		struct.sort(reverse=True);
#		print struct, senatorCount;

		if senatorCount > 0 and (2*struct[1][0] <= senatorCount-1):
			outputStr += chr(ord('A') + struct[0][1]);
			senatorCount -= 1;
			struct[0][0] -= 1;
			struct.sort(reverse=True);

		outputStr += ' ';
#		print struct, senatorCount;

	print("Case #%d: %s" %(i+1, outputStr) );
