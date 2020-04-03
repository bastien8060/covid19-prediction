#!/bin/bash
if [[ -z $1 ]]; then 
	echo "No country supplied. Use -A for all of them"
else
	rm ./data/$1/*
	rm ./imports/$1/*
fi