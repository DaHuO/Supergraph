import sys

def fractiles(argv):
	with open(argv[0], 'r') as f:
		t = int(f.readline())
		for i in range(t):
			k, c, s = f.readline().strip().split()
			if int(k)/int(c) > int(s):
				print "Case #%d: IMPOSSIBLE" % (i+1)
				continue
			# elif int(k) == 1:
			# 	print "Case #%d: 1" % (i+1)
			else:
				print "Case #%d:" % (i+1), " ".join([str(x) for x in range(1,int(k) + 1)])
			# tiles = ["G","L"]
			# l = 0
			# while l < int(k)-1:
			# 	temp = tiles
			# 	tiles = []
			# 	for x in temp:
			# 		tiles.append(x+"G")
			# 		tiles.append(x+"L")
			# 	l = l + 1
			# #print tiles
			# oritiles = tiles
			# for dup in range(int(c)-1):
			# 	temp = tiles
			# 	tiles = []
			# 	for idx, tile in enumerate(temp):
			# 		evotile = ""
			# 		for bit in tile:
			# 			if bit == "L":
			# 				evotile = evotile + oritiles[idx]
			# 			else:
			# 				evotile = evotile + ("G" * len(oritiles[idx]))
			# 		tiles.append(evotile)
			# caltable = [[] for t in tiles]
			# tracebacktable = [[] for t in tiles]
			# for idx, x in enumerate(tiles):
			# 	if idx > 0:
			# 		mincal = min(caltable[idx-1])
			# 	else:
			# 		mincal = 1
			# 	for jdx, y in enumerate(x):
			# 		if idx == 0:
			# 			caltable[idx].append(1)
			# 			tracebacktable[idx].append(jdx)
			# 		else:
			# 			if y == "G":
			# 				if tiles[idx-1][jdx] == y:
			# 					caltable[idx].append(caltable[idx-1][jdx])
			# 					tracebacktable[idx].append(jdx)
			# 				else:
			# 					minjdx = caltable[idx-1].index(mincal)
			# 					caltable[idx].append(mincal + 1)
			# 					tracebacktable[idx].append(minjdx)
			# 			else:
			# 				caltable[idx].append('-')
			# 				tracebacktable[idx].append(jdx)
			# # 	print "".join([str(z) for z in caltable[idx]])
			# # print "\n".join(tiles)
			# #print idx
			# traceback = idx - 1
			# mintile = min(caltable[traceback])
			# minjdx = caltable[traceback].index(mintile)
			# sol = [minjdx]
			# mintile = mintile - 1
			# while mintile > 0:
			# 	# print traceback, minjdx, mintile
			# 	if minjdx not in sol:
			# 		sol.append(minjdx)
			# 		mintile = mintile - 1
			# 	minjdx = tracebacktable[traceback][minjdx]
			# 	traceback = traceback - 1
			# print " ".join([str(z + 1) for z in sol])


if __name__ == "__main__":
	fractiles(sys.argv[1:])