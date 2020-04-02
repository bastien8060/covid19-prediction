#!/bin/bash
if [[ -z $1 ]]; then 
	echo "No country supplied. Use -A for all of them"
elif [[ $1 == "-A" ]]; then 
	rm ../data/*
else
	rm ../data/$1/*
fi