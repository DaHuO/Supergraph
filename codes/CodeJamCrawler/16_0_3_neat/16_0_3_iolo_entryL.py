#!/usr/bin/python

jamcoins = [ "10000000000000000000000000000001","10000000000000000000000000000011","10000000000000000000000000000101","10000000000000000000000000000111","10000000000000000000000000001101","10000000000000000000000000010001","10000000000000000000000000010011","10000000000000000000000000011001","10000000000000000000000000011101","10000000000000000000000000011111","10000000000000000000000000100001","10000000000000000000000000100101","10000000000000000000000000101011","10000000000000000000000000101111","10000000000000000000000000110001","10000000000000000000000000110111","10000000000000000000000000111001","10000000000000000000000000111011","10000000000000000000000000111101","10000000000000000000000001000011","10000000000000000000000001000111","10000000000000000000000001001001","10000000000000000000000001001011","10000000000000000000000001001111","10000000000000000000000001010111","10000000000000000000000001011011","10000000000000000000000001011101","10000000000000000000000001100001","10000000000000000000000001100111","10000000000000000000000001101011","10000000000000000000000001101101","10000000000000000000000001101111","10000000000000000000000001110011","10000000000000000000000001110101","10000000000000000000000001110111","10000000000000000000000001111001","10000000000000000000000001111111","10000000000000000000000010000101","10000000000000000000000010001001","10000000000000000000000010001111","10000000000000000000000010010001","10000000000000000000000010010011","10000000000000000000000010010101","10000000000000000000000010010111","10000000000000000000000010011001","10000000000000000000000010011101","10000000000000000000000010100011","10000000000000000000000010100111","10000000000000000000000010101101","10000000000000000000000010110001","10000000000000000000000010110101","10000000000000000000000010110111","10000000000000000000000011000001","10000000000000000000000011000111","10000000000000000000000011001011","10000000000000000000000011001101","10000000000000000000000011010011","10000000000000000000000011010101","10000000000000000000000011011001","10000000000000000000000011011111","10000000000000000000000011100001","10000000000000000000000011100011","10000000000000000000000011100101","10000000000000000000000011101101","10000000000000000000000011110001","10000000000000000000000011110111","10000000000000000000000011111011","10000000000000000000000011111101","10000000000000000000000100000001","10000000000000000000000100000011","10000000000000000000000100001001","10000000000000000000000100001111","10000000000000000000000100010001","10000000000000000000000100010011","10000000000000000000000100010101","10000000000000000000000100011011","10000000000000000000000100011101","10000000000000000000000100100001","10000000000000000000000100100111","10000000000000000000000100101001","10000000000000000000000100101011","10000000000000000000000100101101","10000000000000000000000100110011","10000000000000000000000100110101","10000000000000000000000100111001","10000000000000000000000100111111","10000000000000000000000101000111","10000000000000000000000101001011","10000000000000000000000101010101","10000000000000000000000101100011","10000000000000000000000101100101","10000000000000000000000101101001","10000000000000000000000101101111","10000000000000000000000101110001","10000000000000000000000101110101","10000000000000000000000101111011","10000000000000000000000101111111","10000000000000000000000110000001","10000000000000000000000110000111","10000000000000000000000110001101","10000000000000000000000110010001","10000000000000000000000110010011","10000000000000000000000110010101","10000000000000000000000110011001","10000000000000000000000110011111","10000000000000000000000110100001","10000000000000000000000110100011","10000000000000000000000110100101","10000000000000000000000110101001","10000000000000000000000110110001","10000000000000000000000110110111","10000000000000000000000110111101","10000000000000000000000111000001","10000000000000000000000111000011","10000000000000000000000111000101","10000000000000000000000111000111","10000000000000000000000111001001","10000000000000000000000111001111","10000000000000000000000111010011","10000000000000000000000111011011","10000000000000000000000111011111","10000000000000000000000111100001","10000000000000000000000111100111","10000000000000000000000111101101","10000000000000000000000111101111","10000000000000000000000111110011","10000000000000000000000111110101","10000000000000000000000111111001","10000000000000000000000111111101","10000000000000000000000111111111","10000000000000000000001000000101","10000000000000000000001000001101","10000000000000000000001000001111","10000000000000000000001000010001","10000000000000000000001000010111","10000000000000000000001000011011","10000000000000000000001000011101","10000000000000000000001000100011","10000000000000000000001000100111","10000000000000000000001000101001","10000000000000000000001000101101","10000000000000000000001000110011","10000000000000000000001000110101","10000000000000000000001000111001","10000000000000000000001000111011","10000000000000000000001001000001","10000000000000000000001001000011","10000000000000000000001001000111","10000000000000000000001001001011","10000000000000000000001001001101","10000000000000000000001001010011","10000000000000000000001001010101","10000000000000000000001001011001","10000000000000000000001001011101","10000000000000000000001001011111","10000000000000000000001001100101","10000000000000000000001001101001","10000000000000000000001001110001","10000000000000000000001001110011","10000000000000000000001001110111","10000000000000000000001001111011","10000000000000000000001001111101","10000000000000000000001010000001","10000000000000000000001010000101","10000000000000000000001010000111","10000000000000000000001010001001","10000000000000000000001010001101","10000000000000000000001010010101","10000000000000000000001010011111","10000000000000000000001010100101","10000000000000000000001010100111","10000000000000000000001010101111","10000000000000000000001010111001","10000000000000000000001011000011","10000000000000000000001011000101","10000000000000000000001011000111","10000000000000000000001011001001","10000000000000000000001011010001","10000000000000000000001011010011","10000000000000000000001011010111","10000000000000000000001011011011","10000000000000000000001011011101","10000000000000000000001011100001","10000000000000000000001011100111","10000000000000000000001011101011","10000000000000000000001011110101","10000000000000000000001011111011","10000000000000000000001011111111","10000000000000000000001100000001","10000000000000000000001100000101","10000000000000000000001100000111","10000000000000000000001100001011","10000000000000000000001100001101","10000000000000000000001100010011","10000000000000000000001100010101","10000000000000000000001100011001","10000000000000000000001100011011","10000000000000000000001100011111","10000000000000000000001100100011","10000000000000000000001100100101","10000000000000000000001100110001","10000000000000000000001100110111","10000000000000000000001100111101","10000000000000000000001100111111","10000000000000000000001101000011","10000000000000000000001101000101","10000000000000000000001101001001","10000000000000000000001101001111","10000000000000000000001101010101","10000000000000000000001101011011","10000000000000000000001101011111","10000000000000000000001101100001","10000000000000000000001101100011","10000000000000000000001101100111","10000000000000000000001101101101","10000000000000000000001101110011","10000000000000000000001101110101","10000000000000000000001101110111","10000000000000000000001101111001","10000000000000000000001101111111","10000000000000000000001110000001","10000000000000000000001110000011","10000000000000000000001110000101","10000000000000000000001110010001","10000000000000000000001110010111","10000000000000000000001110011011","10000000000000000000001110011101","10000000000000000000001110100001","10000000000000000000001110101011","10000000000000000000001110101101","10000000000000000000001110101111","10000000000000000000001110110101","10000000000000000000001110110111","10000000000000000000001110111101","10000000000000000000001110111111","10000000000000000000001111000001","10000000000000000000001111000111","10000000000000000000001111001101","10000000000000000000001111010011","10000000000000000000001111010101","10000000000000000000001111011001","10000000000000000000001111011111","10000000000000000000001111100011","10000000000000000000001111100101","10000000000000000000001111100111","10000000000000000000001111101111","10000000000000000000001111110001","10000000000000000000001111110101","10000000000000000000001111110111","10000000000000000000001111111001","10000000000000000000001111111011","10000000000000000000001111111101","10000000000000000000010000000001","10000000000000000000010000000011","10000000000000000000010000001001","10000000000000000000010000001111","10000000000000000000010000010101","10000000000000000000010000010111","10000000000000000000010000011011","10000000000000000000010000011101","10000000000000000000010000100001","10000000000000000000010000100111","10000000000000000000010000101011","10000000000000000000010000101101","10000000000000000000010000110011","10000000000000000000010000110101","10000000000000000000010000110111","10000000000000000000010000111001","10000000000000000000010000111111","10000000000000000000010001001011","10000000000000000000010001001101","10000000000000000000010001010001","10000000000000000000010001010011","10000000000000000000010001010101","10000000000000000000010001011001","10000000000000000000010001011101","10000000000000000000010001100011","10000000000000000000010001100101","10000000000000000000010001101001","10000000000000000000010001101111","10000000000000000000010001110001","10000000000000000000010001110011","10000000000000000000010001111011","10000000000000000000010010000001","10000000000000000000010010000111","10000000000000000000010010001101","10000000000000000000010010010011","10000000000000000000010010011001","10000000000000000000010010011011","10000000000000000000010010011111","10000000000000000000010010100011","10000000000000000000010010100101","10000000000000000000010010101001","10000000000000000000010010101101","10000000000000000000010010110001","10000000000000000000010010110111","10000000000000000000010010111101","10000000000000000000010010111111","10000000000000000000010011000011","10000000000000000000010011001001","10000000000000000000010011001111","10000000000000000000010011010001","10000000000000000000010011011011","10000000000000000000010011100001","10000000000000000000010011100111","10000000000000000000010011101101","10000000000000000000010011110011","10000000000000000000010011111001","10000000000000000000010011111111","10000000000000000000010100000111","10000000000000000000010100001011","10000000000000000000010100001101","10000000000000000000010100001111","10000000000000000000010100010001","10000000000000000000010100011001","10000000000000000000010100100011","10000000000000000000010100100101","10000000000000000000010100101001","10000000000000000000010100101111","10000000000000000000010100110001","10000000000000000000010100110101","10000000000000000000010100111011","10000000000000000000010101000001","10000000000000000000010101000011","10000000000000000000010101000101","10000000000000000000010101000111","10000000000000000000010101001101","10000000000000000000010101001111","10000000000000000000010101010101","10000000000000000000010101010111","10000000000000000000010101011001","10000000000000000000010101011011","10000000000000000000010101100001","10000000000000000000010101100011","10000000000000000000010101100111","10000000000000000000010101101011","10000000000000000000010101101111","10000000000000000000010101110101","10000000000000000000010101111101","10000000000000000000010101111111","10000000000000000000010110000011","10000000000000000000010110000101","10000000000000000000010110001001","10000000000000000000010110001011","10000000000000000000010110001111","10000000000000000000010110010101","10000000000000000000010110011011","10000000000000000000010110100001","10000000000000000000010110100011","10000000000000000000010110100111","10000000000000000000010110101101","10000000000000000000010110110011","10000000000000000000010110111001","10000000000000000000010110111101","10000000000000000000010110111111","10000000000000000000010111001011","10000000000000000000010111010011","10000000000000000000010111100011","10000000000000000000010111101001","10000000000000000000010111101101","10000000000000000000010111101111","10000000000000000000010111110111","10000000000000000000010111111011","10000000000000000000011000000001","10000000000000000000011000000011","10000000000000000000011000000111","10000000000000000000011000001001","10000000000000000000011000001011","10000000000000000000011000001101","10000000000000000000011000010011","10000000000000000000011000010101","10000000000000000000011000011001","10000000000000000000011000011111","10000000000000000000011000100101","10000000000000000000011000101001","10000000000000000000011000101011","10000000000000000000011000110001","10000000000000000000011000110111","10000000000000000000011000111011","10000000000000000000011000111101","10000000000000000000011001000011","10000000000000000000011001001001","10000000000000000000011001001111","10000000000000000000011001010001","10000000000000000000011001010101","10000000000000000000011001011011","10000000000000000000011001011111","10000000000000000000011001100001","10000000000000000000011001100101","10000000000000000000011001100111","10000000000000000000011001101001","10000000000000000000011001101101","10000000000000000000011001110011","10000000000000000000011001110101","10000000000000000000011001111001","10000000000000000000011001111111","10000000000000000000011010000011","10000000000000000000011010000101","10000000000000000000011010000111","10000000000000000000011010001001","10000000000000000000011010001011","10000000000000000000011010001111","10000000000000000000011010010001","10000000000000000000011010010011","10000000000000000000011010010111","10000000000000000000011010011101","10000000000000000000011010100001","10000000000000000000011010100111","10000000000000000000011010101001","10000000000000000000011010101011","10000000000000000000011010101111","10000000000000000000011010110101","10000000000000000000011010111011","10000000000000000000011010111111","10000000000000000000011011000001","10000000000000000000011011000111","10000000000000000000011011001101","10000000000000000000011011001111","10000000000000000000011011010011","10000000000000000000011011010101","10000000000000000000011011011001","10000000000000000000011011011111","10000000000000000000011011100101","10000000000000000000011011100111","10000000000000000000011011110001","10000000000000000000011011110111","10000000000000000000011011111011","10000000000000000000011011111101","10000000000000000000011100000011","10000000000000000000011100000101","10000000000000000000011100001001","10000000000000000000011100001101","10000000000000000000011100001111","10000000000000000000011100011011","10000000000000000000011100011101","10000000000000000000011100100001","10000000000000000000011100100111","10000000000000000000011100101011","10000000000000000000011100101101","10000000000000000000011100101111","10000000000000000000011100110011","10000000000000000000011100110101","10000000000000000000011100111001","10000000000000000000011100111101","10000000000000000000011100111111","10000000000000000000011101000001","10000000000000000000011101000101","10000000000000000000011101001001","10000000000000000000011101001011","10000000000000000000011101010001","10000000000000000000011101010101","10000000000000000000011101010111","10000000000000000000011101011111","10000000000000000000011101100011","10000000000000000000011101100111","10000000000000000000011101101001","10000000000000000000011101101111","10000000000000000000011101110101","10000000000000000000011101111011","10000000000000000000011101111101","10000000000000000000011110000001","10000000000000000000011110000111","10000000000000000000011110001101","10000000000000000000011110010011","10000000000000000000011110011001","10000000000000000000011110011101","10000000000000000000011110011111","10000000000000000000011110100101","10000000000000000000011110101101","10000000000000000000011110101111","10000000000000000000011110110001","10000000000000000000011110110101","10000000000000000000011110110111","10000000000000000000011110111101","10000000000000000000011111000011","10000000000000000000011111001001","10000000000000000000011111001111","10000000000000000000011111010111","10000000000000000000011111011011","10000000000000000000011111011101","10000000000000000000011111011111","10000000000000000000011111100001","10000000000000000000011111100101","10000000000000000000011111100111","10000000000000000000011111101011","10000000000000000000011111101101","10000000000000000000011111101111","10000000000000000000011111110011","10000000000000000000011111110101","10000000000000000000011111111001","10000000000000000000011111111111","10000000000000000000100000000001","10000000000000000000100000000101","10000000000000000000100000001111","10000000000000000000100000010001","10000000000000000000100000010101","10000000000000000000100000010111","10000000000000000000100000011101","10000000000000000000100000100001","10000000000000000000100000100111"]

print "Case #1:"

for coin in jamcoins:
	line = coin
	for base in xrange(2,11):
		number=int(coin,base)
		for divi in xrange(2,100000): 
			# limit to 100000 because when calculating the jamcoins, pseudo primality test returned 
			# true after 100000 iterations, so i know that the divisor wont be larger than 100000 
			if number % divi == 0:
				line = line + " " + str(divi)
				break
	print line
