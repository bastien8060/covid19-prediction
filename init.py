#!/bin/python
from pandas import read_csv
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.ar_model import ARResults
import numpy
import sys
import os.path
from os import path

if len(sys.argv) < 2:
	print("Select a country");

else:
	os.system("utils/genImport.py "+sys.argv[1].lower())

	if not path.exists("data/"+sys.argv[1].lower()):
		os.mkdir("data/"+sys.argv[1].lower())
	if not path.exists("imports/"+sys.argv[1].lower()):
		os.mkdir("imports/"+sys.argv[1].lower())

	def difference(dataset):
		diff = list()
		for i in range(1, len(dataset)):
			value = dataset[i] - dataset[i - 1]
			diff.append(value)
		return numpy.array(diff)

	# load dataset
	series = read_csv('imports/'+sys.argv[1].lower()+'/data.csv', header=0, index_col=0)
	X = difference(series.values)
	# fit model
	model = AR(X)
	model_fit = model.fit(maxlag=6, disp=False)
	# save model to file
	model_fit.save('data/'+sys.argv[1].lower()+'/ar_model.pkl')
	# save the differenced dataset
	numpy.save('data/'+sys.argv[1].lower()+'/ar_data.npy', X)
	# save the last ob
	numpy.save('data/'+sys.argv[1].lower()+'/ar_obs.npy', [series.values[-1]])

