This piece of code can perform a Huffman encoding on code.
This code can take command line input argument for either 'line' or 'word'.
'line' will make line of the code the unit of encoding, while 'word' will make 
each word of the code that is splited by space the unit of encoding.
The input tests are stored in test_codes folder and the encoding result are in
test_results.


Feb 22 2016
Command input change to :
	python HuffmanString.py \[path\] \[mode\]
path refer to the code path. It could be the path of a specific code or the path of a directory.
mode refer to the unit of encoding. It could be 'line' or 'word'. 
