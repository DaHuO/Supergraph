#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SmithWaterman import SWcompare

def detectLinks(code, codereps, coderepmanager, coderecords, minortokens, codeminorreps, threshold):
	links = {}
	sameraretoken = {}
	used = []
	for line in codereps.keys():
		codelength = len(coderecords[code][line])
		ct = int(codelength * threshold)
		for token in codereps[line]:
			for (f,line2) in coderepmanager[token]:
				if f == code:
					continue
				if (f, line2) in used:
					continue
				used.append((f, line2))
				if len(coderecords[f][line2])<ct:
					continue
				else:
					if SWcompare(coderecords[code][line], coderecords[f][line2]):
						if line in links.keys():
							links[line].append((f, line2))
						else:
							links[line] = []
							links[line].append((f, line2))
	for line in codeminorreps.keys():
		for token in codeminorreps[line]:
			for (f, line2) in minortokens[token]:
				if f == code:
					continue
				elif (f, line2) in links or (f, line2) in sameraretoken:
					continue
				else:
					if line2 in sameraretoken.keys():
						sameraretoken[line].append((f, line2))
					else:
						sameraretoken[line] = []
						sameraretoken[line].append((f, line2))

	return links, sameraretoken

