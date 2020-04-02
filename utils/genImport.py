#!/bin/python
import json
import requests
import sys
import os
import os.path
from os import path

if len(sys.argv) < 2:
	print("Select a country");

else:
	if not path.exists("./imports/"+sys.argv[1].lower()):
		os.mkdir("./imports/"+sys.argv[1].lower())
	filen = "./imports/"+sys.argv[1].lower()+"/data.csv"
	with open(filen, "w+") as fh:
		p=1
	os.chmod(filen, 0o777)

	f = open(filen, 'a')
	x = requests.get('https://pomber.github.io/covid19/timeseries.json')
	y = json.loads(x.text)
	arg = sys.argv[1].capitalize()
	l = len(y[sys.argv[1].capitalize()])
	r = 0
	#print('Dates,Cases')
	f.write('Dates,Cases\n')
	for _ in range(l):
		con = str(y[arg][r]["confirmed"])
		date = str(y[arg][r]["date"])
		line = date+","+con
		#print(line)
		f.write(line+"\n")
		r = r + 1
	f.close()
	print("Success")