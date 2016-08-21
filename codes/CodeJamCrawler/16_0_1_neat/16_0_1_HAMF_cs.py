#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

casesnumber=int(raw_input())
numerodocaso=1

#print casesnumber

def tudoauns(dicionario):
	tudoauns=1
	for coiso in dicionario.values():
		if coiso!=1:
			tudoauns=0
	return tudoauns

lista=list()

while (numerodocaso<=casesnumber):
	linha=raw_input()
	lista.append(int(linha))
	numerodocaso+=1

#print lista

numerodocaso=1

for numero in lista:

	if numero==0:
		print "Case #%d: INSOMNIA"%numerodocaso
		numerodocaso+=1

	else:
		print "Case #%d:"%numerodocaso,
		numerodocaso+=1
		dicio=dict() #dicionario q tem como chaves os numeros de 0 a 9
		multiplica=1
		temp=list()
		res=0
		for i in xrange(0,10):
			dicio[i]=0 #tudo desligado
		while (tudoauns(dicio)!=1):
			res=numero*multiplica
			multiplica+=1
			temp=[int(i) for i in str(res)]
			#print temp
			for elem in temp:
				dicio[elem]=1
			if (tudoauns(dicio)):
				print res
			del temp[:]
			#print dicio