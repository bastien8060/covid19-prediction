#!/bin/bash
if [[ -z $1 ]]; then 
	echo "No country supplied. Use -A for all of them"
else
	./erase.sh $1
	rm -rf ../imports/$1
	rm -rf ../data/$1 
fi
