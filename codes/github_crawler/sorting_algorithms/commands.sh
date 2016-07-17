#! /bin/bash
FILE=./record.txt
while read line; do
	cp $line ./sort_codes/
done < $FILE