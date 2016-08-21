#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2


def getFirstPage(start_page):
	results = []
	response = urllib2.urlopen(start_page)
	html = response.read()
	flag = html.find('. <a href=')
	while flag!=-1:
		flag_end = html.find('"', flag + 12)
		link = html[flag + 11:flag_end].replace("&amp;", ";")
		results.append(link)
		flag = html.find('. <a href=', flag_end)
	return results

def getRestPage(rest_page_prefix, total_page):
	results = []
	page = 1
	while page <= total_page:
		print page
		link = rest_page_prefix + str(page)
		response = urllib2.urlopen(link)
		html = response.read()
		flag = html.find('. <a href=')
		while flag!=-1:
			flag_end = html.find('"', flag + 12)
			link = html[flag + 11:flag_end].replace("&amp;", ";")
			results.append(link)
			flag = html.find('. <a href=', flag_end)
		page += 1
	return results

if __name__ == '__main__':
	start_page = 'https://www.go-hero.net/jam/16/solutions/4/3/Python'
	rest_page_prefix = 'https://www.go-hero.net/jam/16/solutions/4/3/Python/partial/'
	total_rest_page = 0
	results = []
	results.extend(getFirstPage(start_page))
	results.extend(getRestPage(rest_page_prefix, total_rest_page))
	# print results
	file_out = open('links_16_4_3.txt', 'w')
	for link in results:
		file_out.write(link + '\n')
	file_out.close()
