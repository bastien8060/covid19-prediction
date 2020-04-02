#!/bin/python
from statsmodels.tsa.ar_model import ARResults
import numpy
import sys

if len(sys.argv) < 2:
	print("Select a country");

else:
	model = ARResults.load('data/'+sys.argv[1]+'/ar_model.pkl')
	data = numpy.load('data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('data/'+sys.argv[1]+'/ar_obs.npy')
	predictions = model.predict(start=len(data), end=len(data))
	yhat = predictions[0] + last_ob[0]
	print('Prediction: %f' % yhat)
